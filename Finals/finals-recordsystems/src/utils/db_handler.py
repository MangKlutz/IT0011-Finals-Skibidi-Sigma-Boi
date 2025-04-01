import json
import os
import logging
from datetime import datetime

class DatabaseHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def save_record(self, record):
        try:
            records = self.get_all_records()
            record['created_at'] = datetime.now().isoformat()
            records.append(record)
            with open(self.file_path, 'w') as f:
                json.dump(records, f, indent=4)
            return True
        except Exception as e:
            logging.error(f"Error saving record: {e}")
            raise

    def get_all_records(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Error reading records: {e}")
            return []

    def search_records(self, criteria):
        records = self.get_all_records()
        results = []
        for record in records:
            if all(record.get(key, '').lower().startswith(str(value).lower()) 
                for key, value in criteria.items()):
                results.append(record)
        return results

    def delete_record(self, index):
        try:
            records = self.get_all_records()
            if 0 <= index < len(records):
                del records[index]
                with open(self.file_path, 'w') as f:
                    json.dump(records, f, indent=4)
                return True
            return False
        except Exception as e:
            logging.error(f"Error deleting record: {e}")
            raise

    def reset_records(self):
        try:
            with open(self.file_path, 'w') as f:
                json.dump([], f)
            return True
        except Exception as e:
            logging.error(f"Error resetting records: {e}")
            raise