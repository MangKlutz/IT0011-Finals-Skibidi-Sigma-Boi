# src/controllers/user_controller.py

from models.user import User
from utils.db_handler import DatabaseHandler
import os

class UserController:
    def __init__(self):
        self.db = DatabaseHandler(os.path.join('data', 'records.json'))

    def sign_up(self, first_name, middle_name, last_name, birthday, gender):
        try:
            new_user = User(first_name, middle_name, last_name, birthday, gender)
            return self.db.save_record(new_user.to_dict())
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def view_all_records(self):
        return self.db.get_all_records()

    def search_record(self, last_name):
        return self.db.search_records({'last_name': last_name})

    def delete_record(self, index):
        return self.db.delete_record(index)

    def reset_records(self):
        return self.db.reset_records()