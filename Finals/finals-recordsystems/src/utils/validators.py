import re
from datetime import datetime

def validate_name(name):
    if name.upper() == "N/A":
        return "N/A"
    if not name or not name.strip():
        raise ValueError("Name cannot be empty.\nPlease enter a valid name using letters only or 'N/A' if not applicable.")
    if not re.match("^[A-Za-z ]+$", name):
        raise ValueError("Name can only contain letters and spaces or 'N/A' if not applicable.\nExample: John Smith")
    if len(name.strip()) < 2:
        raise ValueError("Name must be at least 2 characters long or 'N/A' if not applicable.\nExample: Li or John")
    if len(name.strip()) > 50:
        raise ValueError("Name is too long (maximum 50 characters).\nPlease enter a shorter name.")
    return name.strip()

def validate_date(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        if date > datetime.now():
            raise ValueError("Birthday cannot be in the future.\nPlease enter a valid past date.\nExample: 1990-01-31")
        min_date = datetime(1900, 1, 1)
        if date < min_date:
            raise ValueError("Birthday must be after 1900-01-01.\nPlease enter a more recent date.")
        return date_str
    except ValueError as e:
        if "does not match format" in str(e):
            raise ValueError("Please enter the date in YYYY-MM-DD format.\nExample: 1990-01-31")
        raise ValueError(str(e))

def validate_gender(gender):
    valid_genders = ["Male", "Female"]
    if gender not in valid_genders:
        raise ValueError("Please select either 'Male' or 'Female'")
    return gender

def validate_email(email):
    if not email:
        return ""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValueError("Invalid email format")
    return email

def validate_phone(phone):
    if not phone:
        return ""
    pattern = r'^\+?1?\d{9,15}$'
    if not re.match(pattern, phone):
        raise ValueError("Invalid phone number format")
    return phone
