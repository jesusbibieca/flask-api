import psycopg2
from psycopg2.extras import RealDictCursor, execute_values
import os
import simplejson as json

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DB_URI")


class PostgresWrapper:
    def __init__(self, **args):
        print(args)
        self.db_url = args.get("DB_URI", DATABASE_URL)
        self.connection = None

    def connect(self):
        pg_conn = psycopg2.connect(self.db_url)
        self.connection = pg_conn

    def get_json_cursor(self):
        return self.connection.cursor(cursor_factory=RealDictCursor)

    @staticmethod
    def execute_and_fetch(cursor, query):
        cursor.execute(query)
        res = cursor.fetchall()
        cursor.close()
        return res

    def get_json_response(self, query):
        cursor = self.get_json_cursor()
        response = self.execute_and_fetch(cursor, query)
        return json.loads(json.dumps(response, default=str))

    def insert_many(self, query, data):
        cursor = self.get_json_cursor()
        execute_values(cursor, query, data, template=None, page_size=100, fetch=False)
        self.connection.commit()
        cursor.close()


def get_db_connection():
    dbconn = PostgresWrapper()
    dbconn.connect()

    return dbconn
