#!/usr/bin/env python3
"""
Simple backend startup script
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables from the project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_file_path = os.path.join(project_root, '.env')
load_dotenv(env_file_path)

# Add the project root to the Python path so imports work correctly
sys.path.insert(0, project_root)

# Now run the backend
if __name__ == "__main__":
    import uvicorn
    # Import the app after setting up the path
    from backend.src.main_with_env import app
    uvicorn.run(app, host="0.0.0.0", port=8002)