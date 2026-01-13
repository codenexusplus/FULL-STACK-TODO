#!/usr/bin/env python3
"""Debug script to check for Pydantic errors"""

import sys
import traceback
import os
sys.path.insert(0, '.')

# Add the backend directory to the path
os.chdir(os.path.join(os.path.dirname(__file__), 'backend'))

try:
    print("Checking Pydantic version...")
    import pydantic
    print(f"Pydantic version: {pydantic.__version__}")
    
    print("\nTesting import of SQLModel...")
    from sqlmodel import SQLModel, Field
    print("✓ SQLModel imported successfully")
    
    print("\nTesting import of user model...")
    from src.models.user import User
    print("✓ User model imported successfully")
    
    print("\nTesting import of todo model...")
    from src.models.todo import Todo
    print("✓ Todo model imported successfully")
    
    print("\nTesting import of session model...")
    from src.models.session import Session
    print("✓ Session model imported successfully")
    
    print("\nTesting import of main app...")
    from src.main import app
    print("✓ Main app imported successfully")
    
    print("\nAll imports successful!")
    
except Exception as e:
    print(f"✗ Error: {e}")
    print("\nDetailed traceback:")
    traceback.print_exc()