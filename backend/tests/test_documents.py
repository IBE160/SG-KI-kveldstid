from fastapi.testclient import TestClient
import pytest
from unittest.mock import patch, Mock
import importlib # Added for module reloading

@pytest.fixture(autouse=True)
def mock_external_services(monkeypatch):
    # Mock text extraction from PDF
    def mock_pdf_extract_nested(file_stream):
        file_stream.seek(0)
        content = file_stream.read().strip()
        if content == b"":
            return ""
        file_stream.seek(0)
        return "Mock text from PDF"
    monkeypatch.setattr("app.core.parsing.extract_text_from_pdf", mock_pdf_extract_nested)

    # Mock text extraction from TXT
    def mock_txt_extract_nested(file_stream):
        file_stream.seek(0)
        return file_stream.read().decode('utf-8')
    monkeypatch.setattr("app.core.parsing.extract_text_from_txt", mock_txt_extract_nested)

    # Reload the ai_parser module to ensure it picks up TESTING_ENV
    import app.core.ai_parser
    importlib.reload(app.core.ai_parser)

@patch("app.api.endpoints.documents.upload_file_to_s3", return_value="s3://mock-bucket/test-object")
def test_upload_cv_document_txt_success(mock_s3):
    """Test successful upload of a text (.txt) file."""
    client = TestClient(app)
    file_content = b"This is a test CV content in plain text."
    response = client.post(
        "/api/v1/cv_documents",
        files={"file": ("test_cv.txt", file_content, "text/plain")}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["filename"] == "test_cv.txt"
    assert data["content_type"] == "text/plain"
    assert data["raw_text_content"] == file_content.decode('utf-8')
    assert "s3_file_path" in data
    assert data["parsed_sections_json"] == {"extracted_name": "Mock User", "extracted_skill": "Mock Skill"}

@patch("app.api.endpoints.documents.upload_file_to_s3", return_value="s3://mock-bucket/test-object")
def test_upload_cv_document_pdf_success(mock_s3):
    """Test successful upload of a text-based PDF (.pdf) file."""
    client = TestClient(app)
    file_content = b"PDF text content"
    response = client.post(
        "/api/v1/cv_documents",
        files={"file": ("test_cv.pdf", file_content, "application/pdf")}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["filename"] == "test_cv.pdf"
    assert data["content_type"] == "application/pdf"
    assert data["raw_text_content"] == "Mock text from PDF"
    assert "s3_file_path" in data
    assert data["parsed_sections_json"] == {"extracted_name": "Mock User", "extracted_skill": "Mock Skill"}

@patch("app.api.endpoints.documents.upload_file_to_s3", return_value="s3://mock-bucket/test-object")
def test_upload_cv_document_pdf_no_text(mock_s3):
    """Test upload of a PDF (.pdf) file from which no text can be extracted."""
    client = TestClient(app)
    file_content = b"" # Simulate a PDF with no extractable text
    response = client.post(
        "/api/v1/cv_documents",
        files={"file": ("image_based.pdf", file_content, "application/pdf")}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Could not extract text from the PDF. It might be an image-based PDF."

@patch("app.api.endpoints.documents.upload_file_to_s3", return_value="s3://mock-bucket/test-object")
def test_upload_cv_document_unsupported_type(mock_s3):
    """Test upload of an unsupported file type (e.g., .jpg)."""
    client = TestClient(app)
    file_content = b"binary image data"
    response = client.post(
        "/api/v1/cv_documents",
        files={"file": ("test_image.jpg", file_content, "image/jpeg")}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Unsupported file type. Only text/plain (.txt) and application/pdf (.pdf) are allowed."

@patch('app.core.config.settings') # Patch settings to control MAX_FILE_SIZE
@patch("app.api.endpoints.documents.upload_file_to_s3", return_value="s3://mock-bucket/test-object")
def test_upload_cv_document_file_too_large(mock_s3, mock_settings):
    """Test upload of a file that exceeds the maximum allowed size."""
    client = TestClient(app)
    mock_settings.MAX_FILE_SIZE = 100 # Set a small max size for testing
    file_content = b"a" * 101 # Create content slightly larger than limit
    
    response = client.post(
        "/api/v1/cv_documents",
        files={"file": ("large_file.txt", file_content, "text/plain")}
    )
    assert response.status_code == 413
    assert "File size exceeds the limit" in response.json()["detail"]