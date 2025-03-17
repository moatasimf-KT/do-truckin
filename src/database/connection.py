import os
from dotenv import load_dotenv
import psycopg2
from contextlib import contextmanager

load_dotenv()

class DatabaseConnection:
    def __init__(self):
        self.config = {
            'host': os.getenv('DB_HOST'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'database': os.getenv('DB_NAME')
        }
    
    @contextmanager
    def get_connection(self):
        conn = None
        try:
            conn = psycopg2.connect(**self.config)
            yield conn
        finally:
            if conn is not None:
                conn.close() 