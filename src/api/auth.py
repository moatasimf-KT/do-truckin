import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta

load_dotenv()

class AuthService:
    def __init__(self):
        self.jwt_secret = os.getenv('JWT_SECRET_KEY')
        
    def generate_token(self, user_id):
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(days=1)
        }
        return jwt.encode(payload, self.jwt_secret, algorithm='HS256')
    
    def verify_token(self, token):
        try:
            return jwt.decode(token, self.jwt_secret, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return None 