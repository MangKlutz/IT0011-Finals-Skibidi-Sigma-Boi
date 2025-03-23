import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def execute_query(conn, query, params=()):
    """ Execute a single query """
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
    except Error as e:
        print(e)

def fetch_all_records(conn, query):
    """ Fetch all records from the database """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def fetch_record(conn, query, params):
    """ Fetch a single record from the database """
    cursor = conn.cursor()
    cursor.execute(query, params)
    return cursor.fetchone()