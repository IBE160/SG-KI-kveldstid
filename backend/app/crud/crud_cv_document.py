from sqlalchemy.orm import Session
from app.models.cv_document import CvDocument
from app.schemas.cv_document import CvDocumentCreate, CvDocumentUpdate
import logging # Added for logging

logger = logging.getLogger(__name__) # Initialize logger

def create_cv_document(db: Session, cv_document: CvDocumentCreate):
    logger.info("Attempting to create CV document", extra={"filename": cv_document.filename})
    db_cv_document = CvDocument(
        filename=cv_document.filename,
        content_type=cv_document.content_type,
        raw_text_content=cv_document.raw_text_content,
        s3_file_path=cv_document.s3_file_path,
        parsed_sections_json=cv_document.parsed_sections_json,
    )
    try:
        db.add(db_cv_document)
        db.commit()
        db.refresh(db_cv_document)
        logger.info("CV document created successfully", extra={"cv_id": db_cv_document.id, "filename": db_cv_document.filename})
        return db_cv_document
    except Exception as e:
        logger.error("Failed to create CV document", extra={"filename": cv_document.filename, "error": str(e)})
        raise

def get_cv_document(db: Session, cv_id: int):
    logger.debug("Attempting to retrieve CV document", extra={"cv_id": cv_id})
    cv = db.query(CvDocument).filter(CvDocument.id == cv_id).first()
    if cv:
        logger.info("CV document retrieved", extra={"cv_id": cv_id})
    else:
        logger.debug("CV document not found", extra={"cv_id": cv_id})
    return cv

def update_cv_document(db: Session, db_cv_document: CvDocument, cv_document_update: CvDocumentUpdate):
    logger.info("Attempting to update CV document", extra={"cv_id": db_cv_document.id, "update_fields": list(cv_document_update.model_dump(exclude_unset=True).keys())})
    update_data = cv_document_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if field == "parsed_sections_json":
            db_cv_document.parsed_sections_json = value # Explicitly replace JSON content
        else:
            setattr(db_cv_document, field, value)
    try:
        db.add(db_cv_document)
        db.commit()
        db.refresh(db_cv_document)
        logger.info("CV document updated successfully", extra={"cv_id": db_cv_document.id})
        return db_cv_document
    except Exception as e:
        logger.error("Failed to update CV document", extra={"cv_id": db_cv_document.id, "error": str(e)})
        raise