from dotenv import load_dotenv
import os
import boto3
import pandas as pd
import json

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    region_name=os.getenv("AWS_REGION")
)

response = s3.get_object(
    Bucket=os.getenv("BUCKET_NAME"),
    Key="raw/2026/06/10/jobs.json"
)

data = json.loads(
    response["Body"].read().decode("utf-8")
)

df = pd.DataFrame(data["results"])

print(df.head())
print(df.columns)

print(df.columns.tolist())

df = df.drop_duplicates(subset=["id"])

print("Rows after removing duplicates:", len(df))