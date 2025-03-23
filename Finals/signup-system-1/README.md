# Signup System

This project is a Python GUI application that allows users to sign up and manage their records with data persistence using JSON files. 

## Features

- Sign-up form for user information (First name, Middle name, Last name, Birthday, Gender)
- Menu for operations: Sign-up, View all records, Search a record, Exit
- Exception handling for user input
- Capability to show all existing records and search for a particular record

## Project Structure

- `src/data/records.json`: Stores user records in JSON format.
- `src/models/user.py`: Defines the `User` class with properties and validation methods.
- `src/views/main_window.py`: Contains the main GUI window setup and menu.
- `src/views/signup_form.py`: Defines the sign-up form GUI.
- `src/controllers/user_controller.py`: Manages user operations and interactions.
- `src/utils/file_handler.py`: Functions for reading and writing to the JSON file.
- `src/main.py`: Entry point of the application.

## Requirements

To run this project, you need to install the following dependencies:

- [List any specific libraries or frameworks required, e.g., Tkinter, etc.]

## Usage

1. Clone the repository.
2. Install the required dependencies.
3. Run `main.py` to start the application.

## License

This project is licensed under the MIT License.