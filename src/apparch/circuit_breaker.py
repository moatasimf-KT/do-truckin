import os
from dotenv import load_dotenv
import redis
from datetime import datetime, timedelta

load_dotenv()

class CircuitBreaker:
    def __init__(self):
        self.redis_client = redis.Redis(
            host=os.getenv('REDIS_URL').split(':')[0],
            port=int(os.getenv('REDIS_URL').split(':')[1]),
            password=os.getenv('REDIS_PASSWORD')
        )
        
    def record_failure(self, service_name):
        key = f"circuit_breaker:{service_name}:failures"
        self.redis_client.incr(key)
        self.redis_client.expire(key, 60)  # Reset after 1 minute 