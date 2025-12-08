from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    S3_BUCKET: str
    OPENAI_API_KEY: str
    MAX_FILE_SIZE: int = 5 * 1024 * 1024  # 5 MB

    class Config:
        env_file = ".env"

settings = Settings()