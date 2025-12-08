from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.cv_document import Base, CvDocument
from app.crud.crud_cv_document import create_cv_document, get_cv_document, update_cv_document
from app.schemas.cv_document import CvDocumentCreate, CvDocumentUpdate
import pytest

# Setup an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" # Use a file-based SQLite for a more persistent test fixture
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(name="db_session")
def db_session_fixture():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

def test_get_cv_document(db_session):
    # Create a CV document first
    cv_document_create = CvDocumentCreate(
        filename="test_cv.txt",
        content_type="text/plain",
        raw_text_content="some raw text content",
        s3_file_path="s3://test-bucket/test_cv.txt",
        parsed_sections_json={"name": "Test User"}
    )
    created_cv = create_cv_document(db_session, cv_document_create)

    # Now try to retrieve it
    retrieved_cv = get_cv_document(db_session, created_cv.id)

    assert retrieved_cv is not None
    assert retrieved_cv.id == created_cv.id
    assert retrieved_cv.filename == "test_cv.txt"
    assert retrieved_cv.parsed_sections_json == {"name": "Test User"}

def test_get_non_existent_cv_document(db_session):
    retrieved_cv = get_cv_document(db_session, 999) # Non-existent ID
    assert retrieved_cv is None

def test_update_cv_document(db_session):
    # Create a CV document first
    cv_document_create = CvDocumentCreate(
        filename="old_name.txt",
        content_type="text/plain",
        raw_text_content="old raw text",
        s3_file_path="s3://test-bucket/old_name.txt",
        parsed_sections_json={"name": "Old Name", "skills": ["Python"]}
    )
    created_cv = create_cv_document(db_session, cv_document_create)

    # Prepare update data
    cv_document_update = CvDocumentUpdate(
        filename="new_name.pdf",
        parsed_sections_json={"name": "New Name", "email": "new@example.com"}
    )

    # Update the document
    updated_cv = update_cv_document(db_session, created_cv, cv_document_update)

    assert updated_cv.id == created_cv.id
    assert updated_cv.filename == "new_name.pdf"
    assert updated_cv.content_type == "text/plain" # Should remain unchanged
    assert updated_cv.raw_text_content == "old raw text" # Should remain unchanged
    assert updated_cv.parsed_sections_json == {"name": "New Name", "email": "new@example.com"}
    assert updated_cv.s3_file_path == "s3://test-bucket/old_name.txt" # Should remain unchanged

    # Retrieve and verify from database
    retrieved_cv = get_cv_document(db_session, created_cv.id)
    assert retrieved_cv.filename == "new_name.pdf"
    assert retrieved_cv.parsed_sections_json == {"name": "New Name", "email": "new@example.com"}

# def test_update_cv_document_partial(db_session):
#     # Create a CV document first
#     cv_document_create = CvDocumentCreate(
#         filename="partial.txt",
#         content_type="text/plain",
#         raw_text_content="partial raw text",
#         s3_file_path="s3://test-bucket/partial.txt",
#         parsed_sections_json={"name": "Partial User", "skills": ["Java"]}
#     )
#     created_cv = create_cv_document(db_session, cv_document_create)

#     # Prepare partial update data
#     cv_document_update = CvDocumentUpdate(
#         parsed_sections_json={"skills": ["Java", "SQL"]}
#     )

#     # Update the document
#     updated_cv = update_cv_document(db_session, created_cv, cv_document_update)

#     assert updated_cv.id == created_cv.id
#     assert updated_cv.filename == "partial.txt"
#     assert updated_cv.parsed_sections_json == {"skills": ["Java", "SQL"]}

#     # Retrieve and verify from database
#     retrieved_cv = get_cv_document(db_session, created_cv.id)
#     assert retrieved_cv.filename == "partial.txt"
#     assert retrieved_cv.parsed_sections_json == {"name": "Partial User", "skills": ["Java", "SQL"]}
