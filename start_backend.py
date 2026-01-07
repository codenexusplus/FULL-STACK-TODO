#!/usr/bin/env python3
"""
Backend startup script that ensures environment variables are loaded first
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables from the project root
project_root = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(project_root, '.env')
load_dotenv(env_file_path)

print(f"DATABASE_URL from environment: {os.getenv('DATABASE_URL')}")
print(f"API_SECRET_KEY from environment: {os.getenv('API_SECRET_KEY')}")

# Add the backend/src directory to the Python path
backend_src_path = os.path.join(project_root, 'backend', 'src')
sys.path.insert(0, backend_src_path)

# Now import and run the main application
import importlib.util
spec = importlib.util.spec_from_file_location("main", os.path.join(backend_src_path, "main.py"))
main_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(main_module)
app = main_module.app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)