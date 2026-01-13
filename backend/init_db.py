# backend/init_db.py
import logging
from src.database import create_db_and_tables

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_database():
    logger.info("Starting database initialization...")
    try:
        create_db_and_tables()
        logger.info("Database initialization complete.")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
        raise

if __name__ == "__main__":
    initialize_database()
