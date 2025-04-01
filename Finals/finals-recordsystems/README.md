# Signup System

This project is a Python application that provides a graphical user interface (GUI) for managing user records. It includes functionalities for signing up new users, viewing all records, and searching for specific records.

## Features

- **Sign-up Form**: Allows users to enter their first name, middle name, last name, birthday, and gender.
- **View All Records**: Displays all existing user records stored in the database.
- **Search Records**: Enables searching for a specific user record by name.
- **Data Persistence**: User records are stored in a SQLite database.
- **Exception Handling**: The application handles errors gracefully to ensure a smooth user experience.

## Project Structure

- `src/`: Contains the source code for the application.
  - `data/`: Contains the SQLite database file.
  - `models/`: Contains the data models for the application.
  - `views/`: Contains the GUI components.
  - `controllers/`: Contains the logic for managing user operations.
  - `utils/`: Contains utility functions for database operations.
  - `main.py`: The entry point of the application.

## Requirements

To run this project, you need to install the following dependencies:

- `tkinter`: For creating the GUI.
- `sqlite3`: For database operations.

## Usage

1. Clone the repository.
2. Install the required dependencies.
3. Run `main.py` to start the application.

## License

This project is licensed under the MIT License.