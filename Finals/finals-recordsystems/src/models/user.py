from ..utils.validators import validate_name, validate_date, validate_gender

class User:
    def __init__(self, first_name, middle_name, last_name, birthday, gender):
        if first_name.upper() == "N/A":
            raise ValueError("First Name cannot be 'N/A'")
        if last_name.upper() == "N/A":
            raise ValueError("Last Name cannot be 'N/A'")
            
        self.first_name = validate_name(first_name)
        # Handle empty or N/A middle name
        self.middle_name = "N/A" if not middle_name or middle_name.strip() == "" or middle_name.upper() == "N/A" else validate_name(middle_name)
        self.last_name = validate_name(last_name)
        self.birthday = validate_date(birthday)
        self.gender = validate_gender(gender)

    def create_user(self):
        # Logic to create a new user in the database
        pass

    def get_user_data(self):
        # Logic to retrieve user data from the database
        pass

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'middle_name': self.middle_name,
            'last_name': self.last_name,
            'birthday': self.birthday,
            'gender': self.gender
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['first_name'],
            data['middle_name'],
            data['last_name'],
            data['birthday'],
            data['gender']
        )