import os
from dotenv import load_dotenv
import json
import boto3

load_dotenv()

class TelemetryProcessor:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
    
    def process_device_data(self, device_id, telemetry_data):
        # Store raw telemetry data
        self.s3_client.put_object(
            Bucket='iot-telemetry',
            Key=f'raw/{device_id}/{telemetry_data["timestamp"]}.json',
            Body=json.dumps(telemetry_data)
        ) 