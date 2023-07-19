import os
import boto3
from dotenv import load_dotenv
load_dotenv()

class StorageS3Client:
    def __init__(self):
        self.endpoint_url= os.environ.get("STORAGE_URL")
        self.default_region = os.environ.get("STORAGE_DEFAULT_REGION")
        self.aws_access_key_id = os.environ.get("STORAGE_KEY")
        self.aws_secret_access_key = os.environ.get("STORAGE_SECRET")
        self.bucket_name = os.environ.get("STORAGE_BUCKET_NAME")
        self.client = boto3.client(
            's3',
            endpoint_url = self.endpoint_url,  # LocalStack endpoint
            region_name = self.default_region,  # Specify desired region
            aws_access_key_id = self.aws_access_key_id,  # Provide your AWS access key
            aws_secret_access_key = self.aws_secret_access_key  # Provide your AWS secret key
        )

    def upload_fileobj(self, file, filepath):
        self.client.upload_fileobj(file, self.bucket_name, filepath)


    def download(self, filepath):
        self.client.get_object(Bucket=self.bucket_name, Key=filepath)