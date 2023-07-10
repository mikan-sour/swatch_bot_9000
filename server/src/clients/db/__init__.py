import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

class DBClient:
    def __init__(self):
        self.host = os.environ.get("POSTGRES_HOST")
        self.port = os.environ.get("POSTGRES_PORT")
        self.database = os.environ.get("POSTGRES_DB")
        self.user = os.environ.get("POSTGRES_USER")
        self.password = os.environ.get("POSTGRES_PASSWORD")
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to the PostgreSQL database!")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            print("Disconnected from the PostgreSQL database.")

    def execute(self, query, params=None):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
            return cursor
        except (Exception, psycopg2.Error) as error:
            print("Error executing query:", error)