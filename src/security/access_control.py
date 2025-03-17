import os
from dotenv import load_dotenv
from datetime import datetime
import jwt

load_dotenv()

class AccessControl:
    def __init__(self):
        self.jwt_secret = os.getenv('JWT_SECRET_KEY')
        
    def validate_access_token(self, token, required_permissions):
        try:
            decoded = jwt.decode(token, self.jwt_secret, algorithms=['HS256'])
            return all(perm in decoded.get('permissions', []) for perm in required_permissions)
        except:
            return False 