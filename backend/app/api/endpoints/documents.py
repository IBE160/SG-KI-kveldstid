from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends
from sqlalchemy.orm import Session
import io
import uuid
import os
import logging # Added for logging
from typing import Optional
from app.core.parsing import extract_text_from_txt, extract_text_from_pdf
from app.core.ai_parser import extract_structured_data
from app.core.s3 import upload_file_to_s3
from app.core.config import settings
from app.schemas.cv_document import CvDocumentCreate, CvDocument, CvDocumentUpdate
from app.crud import crud_cv_document
from app.db.session import SessionLocal

logger = logging.getLogger(__name__) # Initialize logger

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cv_documents", response_model=CvDocument, summary="Upload a CV document")
async def upload_cv_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Uploads a CV document (text-only PDF or TXT) for parsing and storage.
    """
    logger.info("Received request to upload CV document", extra={"filename": file.filename, "content_type": file.content_type})

    if file.content_type not in ["text/plain", "application/pdf"]:
        logger.warning("Unsupported file type upload attempt", extra={"filename": file.filename, "content_type": file.content_type})
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported file type. Only text/plain (.txt) and application/pdf (.pdf) are allowed."
        )

    file_content = await file.read()
    if len(file_content) > settings.MAX_FILE_SIZE:
        logger.warning("File size exceeds limit", extra={"filename": file.filename, "size": len(file_content)})
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File size exceeds the limit of {settings.MAX_FILE_SIZE // 1024 // 1024} MB."
        )

    file_stream = io.BytesIO(file_content)
    
    try:
        # Generate a secure filename for S3
        file_extension = os.path.splitext(file.filename)[1]
        s3_object_name = f"{uuid.uuid4()}{file_extension}"
        logger.info("Generated S3 object name", extra={"original_filename": file.filename, "s3_object_name": s3_object_name})

        s3_file_path = upload_file_to_s3(
            file_stream,
            bucket_name=settings.S3_BUCKET,
            object_name=s3_object_name,
        )
        if not s3_file_path:
            logger.error("Failed to upload file to S3", extra={"filename": file.filename, "s3_object_name": s3_object_name})
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Could not upload file to S3."
            )
        logger.info("File uploaded to S3 successfully", extra={"filename": file.filename, "s3_path": s3_file_path})

        file_stream.seek(0)
        raw_text_content = ""

        if file.content_type == "text/plain":
            raw_text_content = extract_text_from_txt(file_stream)
        elif file.content_type == "application/pdf":
            raw_text_content = extract_text_from_pdf(file_stream)
            if not raw_text_content.strip():
                logger.warning("No text extracted from PDF", extra={"filename": file.filename})
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Could not extract text from the PDF. It might be an image-based PDF."
                )
        logger.info("Text extracted from CV", extra={"filename": file.filename, "raw_text_length": len(raw_text_content)})

        # Extract structured data using the AI parser
        structured_data = extract_structured_data(raw_text_content)
        logger.info("Structured data extracted from CV", extra={"filename": file.filename, "extracted_keys": list(structured_data.keys())})

        cv_document_in = CvDocumentCreate(
            filename=file.filename, # Keep original filename for user reference
            content_type=file.content_type,
            raw_text_content=raw_text_content,
            s3_file_path=s3_file_path,
            parsed_sections_json=structured_data,
        )
        
        db_cv_document = crud_cv_document.create_cv_document(db=db, cv_document=cv_document_in)
        logger.info("CV document created in DB", extra={"cv_id": db_cv_document.id, "filename": db_cv_document.filename})
        return db_cv_document
    except HTTPException:
        raise # Re-raise HTTPExceptions as they are already handled
    except Exception as e:
        logger.exception("An unexpected error occurred during CV upload", extra={"filename": file.filename}) # Log with traceback
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}"
        )

@router.get("/cv_documents/{cv_id}", response_model=CvDocument, summary="Retrieve a CV document by ID")
def get_cv_document(cv_id: int, db: Session = Depends(get_db)):
    """
    Retrieves a single CV document by its ID.
    """
    logger.info("Received request to retrieve CV document", extra={"cv_id": cv_id})
    db_cv_document = crud_cv_document.get_cv_document(db, cv_id=cv_id)
    if db_cv_document is None:
        logger.warning("CV document not found", extra={"cv_id": cv_id})
        raise HTTPException(status_code=404, detail="CV Document not found")
    logger.info("CV document retrieved successfully", extra={"cv_id": cv_id, "filename": db_cv_document.filename})
    return db_cv_document

@router.put("/cv_documents/{cv_id}", response_model=CvDocument, summary="Update a CV document by ID")
def update_cv_document(cv_id: int, cv_document_update: CvDocumentUpdate, db: Session = Depends(get_db)):
    """
    Updates an existing CV document by its ID.
    """
    logger.info("Received request to update CV document", extra={"cv_id": cv_id, "update_fields": list(cv_document_update.model_dump(exclude_unset=True).keys())})
    db_cv_document = crud_cv_document.get_cv_document(db, cv_id=cv_id)
    if db_cv_document is None:
        logger.warning("Attempted to update non-existent CV document", extra={"cv_id": cv_id})
        raise HTTPException(status_code=404, detail="CV Document not found")
    
    try:
        updated_document = crud_cv_document.update_cv_document(db, db_cv_document=db_cv_document, cv_document_update=cv_document_update)
        logger.info("CV document updated successfully", extra={"cv_id": cv_id, "filename": updated_document.filename})
        return updated_document
    except Exception as e:
        logger.exception("An unexpected error occurred during CV update", extra={"cv_id": cv_id})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}"
        )