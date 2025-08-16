
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

# def getAllData(table):
#     cursor = connection.cursor()
#     cursor.execute(f"SELECT * FROM {table}")
#     data = cursor.fetchall()
#     cursor.close()
#     return data

def getData(table, columns="*", where=None, params=None):
    # Whitelist allowed tables
    allowed_tables = {"artisan", "player", "items", "primary_archetype", "player_artisan"}
    if table not in allowed_tables:
        raise ValueError("Table not allowed.")

    query = f"SELECT {columns} FROM {table}"
    if where:
        query += f" WHERE {where}"

    print(f"Executing query: \n {query} \n with params: {params}")
    cursor = connection.cursor()
    cursor.execute(query, params or {})
    data = cursor.fetchall()
    cursor.close()
    return data