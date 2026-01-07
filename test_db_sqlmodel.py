import os
import sys
from dotenv import load_dotenv

print("Starting database connection test...")

# Load environment variables
load_dotenv()

# Get database URL
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"DATABASE_URL: {DATABASE_URL}")

if not DATABASE_URL:
    print("ERROR: DATABASE_URL is not set in environment variables")
    sys.exit(1)

print("Importing SQLModel components...")
try:
    from sqlmodel import create_engine, select
    print("SQLModel imported successfully")
except ImportError as e:
    print(f"Failed to import SQLModel: {e}")
    sys.exit(1)

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
        
        # Now test with SQLModel models
        print("Testing with SQLModel models...")
        from backend.src.models.user import User
        stmt = select(User).limit(1)
        result = conn.execute(stmt)
        user = result.first()
        print(f"User query result: {user}")
        
except Exception as e:
    print(f"Database connection failed: {e}")
    import traceback
    traceback.print_exc()