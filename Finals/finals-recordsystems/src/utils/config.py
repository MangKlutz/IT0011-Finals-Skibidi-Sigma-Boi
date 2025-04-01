import os

# Database configuration
DB_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'users.db')

# UI Configuration
WINDOW_SIZE = "800x600"
PADDING = 10
BUTTON_WIDTH = 20

# Theme Configuration
COLORS = {
    'primary': '#2196F3',
    'secondary': '#FFC107',
    'error': '#F44336',
    'success': '#4CAF50',
    'background': '#FFFFFF',
    'text': '#000000'
}

# Date format
DATE_FORMAT = '%Y-%m-%d'
