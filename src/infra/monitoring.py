import os
from dotenv import load_dotenv
import requests

load_dotenv()

class MonitoringService:
    def __init__(self):
        self.slack_webhook = os.getenv('SLACK_WEBHOOK_URL')
        
    def alert_incident(self, severity, message, details):
        alert_data = {
            "text": f"🚨 {severity.upper()} Alert",
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": f"*{message}*\n{details}"}
                }
            ]
        }
        
        requests.post(self.slack_webhook, json=alert_data) 