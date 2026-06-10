from dotenv import load_dotenv
from datetime import datetime
import os
import boto3

# Load environment variables
load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY")
aws_secret_key = os.getenv("AWS_SECRET_KEY")
aws_region = os.getenv("AWS_REGION")
bucket_name = os.getenv("BUCKET_NAME")

# Validate credentials
if not aws_access_key or not aws_secret_key:
    raise RuntimeError(
        "Missing AWS_ACCESS_KEY or AWS_SECRET_KEY in the .env file."
    )

# Create S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region,
)

# Create date-based S3 path
today = datetime.now()

s3_key = (
    f"raw/{today.year}/"
    f"{today.month:02d}/"
    f"{today.day:02d}/jobs.json"
)

# Upload file
s3.upload_file(
    "raw/jobs.json",
    bucket_name,
    s3_key
)

print(f"Upload successful!")
print(f"Uploaded to: s3://{bucket_name}/{s3_key}")