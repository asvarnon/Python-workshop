
import cx_Oracle
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT', 1521))
DB_SERVICE = os.getenv('DB_SERVICE')

dsn = cx_Oracle.makedsn(DB_HOST, DB_PORT, service_name=DB_SERVICE)
connection = cx_Oracle.connect(user=DB_USER, password=DB_PASSWORD, dsn=dsn)

def getData(table):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall()
    cursor.close()
    return data