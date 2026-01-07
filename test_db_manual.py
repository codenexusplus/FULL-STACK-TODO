#!/usr/bin/env python3
"""
Test script to verify the backend can reach the Neon database
This version sets the environment variable directly in the script
"""

import os
from pathlib import Path
import sys

# Read the .env file and set environment variables manually
with open('.env', 'r') as f:
    for line in f:
        if line.strip() and not line.startswith('#') and '=' in line:
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip().strip('"\'')  # Remove quotes if present
            os.environ[key] = value
            print(f"Set environment variable {key}={value}")

# Add the backend/src directory to the Python path
backend_src_path = os.path.join(os.path.dirname(__file__), 'backend', 'src')
sys.path.insert(0, backend_src_path)

# Now get the environment variables directly
database_url = os.getenv('DATABASE_URL')
api_secret_key = os.getenv('API_SECRET_KEY')
better_auth_secret = os.getenv('BETTER_AUTH_SECRET')
better_auth_url = os.getenv('BETTER_AUTH_URL')

print(f"\nDATABASE_URL from environment: {database_url}")
print(f"API_SECRET_KEY from environment: {api_secret_key}")
print(f"BETTER_AUTH_SECRET from environment: {better_auth_secret}")
print(f"BETTER_AUTH_URL from environment: {better_auth_url}")

# Now test the database connection
from sqlmodel import create_engine, text

def test_database_connection():
    """Test the database connection using the environment variables"""
    try:
        # Create an engine with the database URL from environment
        engine = create_engine(database_url)
        
        # Try to connect and execute a simple query
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            value = result.scalar()
            
        if value == 1:
            print("SUCCESS: Successfully connected to the Neon database!")
            print(f"Database URL: {database_url}")
            return True
        else:
            print("ERROR: Unexpected result from database query")
            return False
            
    except Exception as e:
        print(f"ERROR: Failed to connect to the database: {str(e)}")
        return False


if __name__ == "__main__":
    print("Testing database connection...")
    success = test_database_connection()
    
    if success:
        print("Database connection test passed!")
    else:
        print("Database connection test failed!")