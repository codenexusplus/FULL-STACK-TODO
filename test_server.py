#!/usr/bin/env python3
"""Test server startup to reproduce the error"""

import sys
import os
import traceback

# Add the backend directory to the path
backend_path = os.path.join(os.path.dirname(__file__), 'backend')
sys.path.insert(0, backend_path)
os.chdir(backend_path)

try:
    print("Attempting to start the server...")
    from src.main import app
    print("App imported successfully")
    
    import uvicorn
    print("Uvicorn imported successfully")
    
    print("Server would start successfully with no errors")
    
except Exception as e:
    print(f"✗ Error starting server: {e}")
    print("\nDetailed traceback:")
    traceback.print_exc()