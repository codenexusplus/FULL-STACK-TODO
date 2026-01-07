import os
import sys
from dotenv import load_dotenv
from sqlmodel import create_engine

print("Starting database connection test...")

# Load environment variables
load_dotenv()

# Get database URL
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"DATABASE_URL: {DATABASE_URL}")

if not DATABASE_URL:
    print("ERROR: DATABASE_URL is not set in environment variables")
    sys.exit(1)
else:
    print("Attempting to create database engine...")
    try:
        # Create engine
        engine = create_engine(DATABASE_URL)
        print("Database engine created successfully")
        
        print("Attempting to connect to database...")
        # Test the connection
        with engine.connect() as conn:
            print("Database connection successful!")
            result = conn.execute("SELECT 1")
            print(f"Test query result: {result.fetchone()}")
    except Exception as e:
        print(f"Database connection failed: {e}")
        import traceback
        traceback.print_exc()