import os
from datetime import datetime
import boto3
from dotenv import load_dotenv

load_dotenv()

class AuditLogger:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        
    def log_security_event(self, event_type, user_id, details):
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'event_type': event_type,
            'user_id': user_id,
            'details': details
        }
        
        self.s3_client.put_object(
            Bucket='security-audit-logs',
            Key=f'logs/{datetime.utcnow().date()}/{event_type}-{datetime.utcnow().timestamp()}.json',
            Body=str(log_entry)
        ) 