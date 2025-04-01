import logging
import os
from datetime import datetime

def setup_logging():
    # Create logs directory if it doesn't exist
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create log file with timestamp
    log_file = os.path.join(log_dir, f'signup_system_{datetime.now().strftime("%Y%m%d")}.log')

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    # Log system startup
    logging.info('Signup System started')
