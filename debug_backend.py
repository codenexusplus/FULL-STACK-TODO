import os
import sys
import traceback
from dotenv import load_dotenv

print("Starting debug of backend...")

try:
    # Load environment variables from the project root
    project_root = os.path.dirname(os.path.abspath(__file__))
    env_file_path = os.path.join(project_root, '.env')
    load_dotenv(env_file_path)

    print(f"Project root: {project_root}")
    print(f"Environment file path: {env_file_path}")
    print(f"DATABASE_URL from env: {os.getenv('DATABASE_URL')}")

    # Add both the project root and the backend directory to the Python path
    sys.path.insert(0, project_root)
    sys.path.insert(0, os.path.join(project_root, 'backend'))

    print(f"Python path: {sys.path[:3]}...")  # Show first 3 entries

    try:
        from fastapi import FastAPI
        print("FastAPI imported successfully")
    except ImportError as e:
        print(f"Error importing FastAPI: {e}")
        traceback.print_exc()

    try:
        from fastapi.middleware.cors import CORSMiddleware
        print("CORS middleware imported successfully")
    except ImportError as e:
        print(f"Error importing CORS middleware: {e}")
        traceback.print_exc()

    try:
        # Import the API routers using absolute imports
        from backend.src.api import auth, todos
        print("Auth and todos imported successfully")
    except ImportError as e:
        print(f"Error importing backend modules: {e}")
        traceback.print_exc()

    try:
        from backend.src.database import create_db_and_tables
        print("Database module imported successfully")
    except ImportError as e:
        print(f"Error importing database module: {e}")
        traceback.print_exc()

    print("Debug completed.")
except Exception as e:
    print(f"Unexpected error during debug: {e}")
    traceback.print_exc()