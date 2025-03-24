import re
from datetime import datetime

def validate_name(name):
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")
    if not re.match("^[A-Za-z ]+$", name):
        raise ValueError("Name can only contain letters and spaces")
    return name.strip()

def validate_date(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        if date > datetime.now():
            raise ValueError("Birthday cannot be in the future")
        return date_str
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD")

def validate_gender(gender):
    valid_genders = ["Male", "Female"]
    if gender not in valid_genders:
        raise ValueError("Invalid gender")
    return gender
