from dotenv import load_dotenv
import os
import boto3

load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY")
aws_secret_key = os.getenv("AWS_SECRET_KEY")
aws_region = os.getenv("AWS_REGION")

if not aws_access_key or not aws_secret_key:
    raise RuntimeError(
        "Missing AWS_ACCESS_KEY or AWS_SECRET_KEY in the .env file."
    )

s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region,
)

s3.upload_file(
    "raw/jobs.json",
    os.getenv("BUCKET_NAME"),
    "raw/jobs.json"
)

print("Upload successful!")