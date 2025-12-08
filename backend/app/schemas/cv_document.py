from pydantic import BaseModel, Field
import datetime
from typing import Optional, List # Removed Dict, Any as it will no longer be needed

class ContactInfo(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class ExperienceItem(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    dates: Optional[str] = None
    description: Optional[str] = None

class EducationItem(BaseModel):
    degree: Optional[str] = None
    university: Optional[str] = None
    year: Optional[int] = None # Assuming year is an integer

class CvParsedData(BaseModel):
    contact_info: Optional[ContactInfo] = None
    summary: Optional[str] = None
    experience: Optional[List[ExperienceItem]] = None
    education: Optional[List[EducationItem]] = None
    skills: Optional[List[str]] = None

class CvDocumentBase(BaseModel):
    filename: str
    content_type: str

class CvDocumentCreate(CvDocumentBase):
    raw_text_content: str
    s3_file_path: str
    parsed_sections_json: Optional[CvParsedData] = None

class CvDocumentUpdate(BaseModel):
    filename: Optional[str] = None
    content_type: Optional[str] = None
    raw_text_content: Optional[str] = None
    s3_file_path: Optional[str] = None
    parsed_sections_json: Optional[CvParsedData] = None

class CvDocument(CvDocumentBase):
    id: int
    s3_file_path: str
    upload_date: datetime.datetime
    parsed_sections_json: Optional[CvParsedData] = None

    class Config:
        orm_mode = True