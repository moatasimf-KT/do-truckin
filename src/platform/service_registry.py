import os
from dotenv import load_dotenv
import psycopg2
import json

load_dotenv()

class ServiceRegistry:
    def __init__(self):
        self.db_config = {
            'host': os.getenv('DB_HOST'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'database': os.getenv('DB_NAME')
        }
    
    def register_service(self, service_name, endpoint, health_check_url):
        with psycopg2.connect(**self.db_config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO service_registry (service_name, endpoint, health_check_url)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (service_name) DO UPDATE
                    SET endpoint = EXCLUDED.endpoint,
                        health_check_url = EXCLUDED.health_check_url
                """, (service_name, endpoint, health_check_url)) 