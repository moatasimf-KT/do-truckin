import os
from dotenv import load_dotenv
import psycopg2
import boto3

load_dotenv()

class ETLPipeline:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        self.db_config = {
            'host': os.getenv('DB_HOST'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'database': os.getenv('DB_NAME')
        }
    
    def extract_from_s3(self, bucket, key):
        response = self.s3_client.get_object(Bucket=bucket, Key=key)
        return response['Body'].read() 