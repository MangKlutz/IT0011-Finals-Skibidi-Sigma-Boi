import sqlite3
from sqlite3 import Error
import logging

class DatabaseHandler:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self._create_tables()

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            self.conn.row_factory = sqlite3.Row
            return self.conn
        except Error as e:
            logging.error(f"Database connection error: {e}")
            raise

    def _create_tables(self):
        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            birthday TEXT NOT NULL,
            gender TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            with self.connect() as conn:
                conn.execute(create_users_table)
        except Error as e:
            logging.error(f"Error creating tables: {e}")
            raise

    def execute_query(self, query, params=()):
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                return cursor.lastrowid
        except Error as e:
            logging.error(f"Query execution error: {e}")
            raise

    def fetch_all(self, query, params=()):
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                return [dict(row) for row in cursor.fetchall()]
        except Error as e:
            logging.error(f"Error fetching records: {e}")
            raise