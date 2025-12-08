from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class CvDocument(Base):
    __tablename__ = "cv_documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    content_type = Column(String)
    raw_text_content = Column(Text)
    parsed_sections_json = Column(JSON, nullable=True)
    s3_file_path = Column(String)
    upload_date = Column(DateTime, default=datetime.datetime.utcnow)