class User:
    def __init__(self, first_name, middle_name, last_name, birthday, gender):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender

    def validate(self):
        if not self.first_name or not self.last_name:
            raise ValueError("First name and last name are required.")
        if self.gender not in ['Male', 'Female', 'Other']:
            raise ValueError("Gender must be 'Male', 'Female', or 'Other'.")
        # Additional validation can be added as needed