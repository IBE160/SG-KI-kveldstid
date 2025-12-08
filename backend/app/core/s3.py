import boto3
from .config import settings

s3_client = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION,
)

def upload_file_to_s3(file_stream, bucket_name, object_name):
    """
    Upload a file to an S3 bucket
    """
    try:
        s3_client.upload_fileobj(file_stream, bucket_name, object_name)
    except Exception as e:
        print(f"Error uploading to S3: {e}")
        return None
    return f"https://{bucket_name}.s3.amazonaws.com/{object_name}"
