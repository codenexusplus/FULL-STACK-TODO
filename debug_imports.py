import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

print("Project root:", project_root)

# Try importing the modules step by step
try:
    from dotenv import load_dotenv
    print("✓ dotenv imported successfully")
except ImportError as e:
    print("✗ Failed to import dotenv:", e)

try:
    load_dotenv(os.path.join(project_root, '.env'))
    print("✓ .env loaded successfully")
except Exception as e:
    print("✗ Failed to load .env:", e)

try:
    from backend.src.api import auth, todos
    print("✓ auth and todos imported successfully")
except ImportError as e:
    print("✗ Failed to import auth or todos:", e)
    import traceback
    traceback.print_exc()

try:
    from backend.src.database import create_db_and_tables
    print("✓ create_db_and_tables imported successfully")
except ImportError as e:
    print("✗ Failed to import create_db_and_tables:", e)
    import traceback
    traceback.print_exc()

try:
    from fastapi import FastAPI
    print("✓ FastAPI imported successfully")
except ImportError as e:
    print("✗ Failed to import FastAPI:", e)