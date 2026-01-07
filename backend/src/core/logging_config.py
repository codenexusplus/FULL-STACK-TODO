import os
from dotenv import load_dotenv

# Load environment variables first
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '.env'))

import logging
import sys
from datetime import datetime
from pathlib import Path

def setup_logging():
    """
    Set up logging configuration for the application.
    """
    # Create logs directory if it doesn't exist
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    # Define log format
    log_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # File handler for general logs
    file_handler = logging.FileHandler(
        logs_dir / f"app_{datetime.now().strftime('%Y%m%d')}.log"
    )
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    # File handler for error logs
    error_handler = logging.FileHandler(
        logs_dir / f"errors_{datetime.now().strftime('%Y%m%d')}.log"
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(log_format)
    logger.addHandler(error_handler)

    return logger