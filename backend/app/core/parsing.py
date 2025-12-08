from PyPDF2 import PdfReader
import io

def extract_text_from_pdf(file_stream: io.BytesIO) -> str:
    """
    Extracts text from a PDF file stream.
    """
    reader = PdfReader(file_stream)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_txt(file_stream: io.BytesIO) -> str:
    """
    Extracts text from a TXT file stream.
    """
    return file_stream.read().decode("utf-8")
