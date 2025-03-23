# src/controllers/user_controller.py

from models.user import User
from utils.db_handler import connect_to_db, execute_query
import sqlite3

class UserController:
    def __init__(self):
        self.connection = connect_to_db()

    def sign_up(self, first_name, middle_name, last_name, birthday, gender):
        try:
            new_user = User(first_name, middle_name, last_name, birthday, gender)
            query = "INSERT INTO users (first_name, middle_name, last_name, birthday, gender) VALUES (?, ?, ?, ?, ?)"
            execute_query(self.connection, query, (new_user.first_name, new_user.middle_name, new_user.last_name, new_user.birthday, new_user.gender))
            return True
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False

    def view_all_records(self):
        try:
            query = "SELECT * FROM users"
            cursor = self.connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []

    def search_record(self, first_name, last_name):
        try:
            query = "SELECT * FROM users WHERE first_name = ? AND last_name = ?"
            cursor = self.connection.cursor()
            cursor.execute(query, (first_name, last_name))
            record = cursor.fetchone()
            return record
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None