#!/usr/bin/env python3
"""Test to reproduce the PydanticUserError"""

import sys
import os
import traceback

# Add the backend directory to the path
backend_path = os.path.join(os.path.dirname(__file__), 'backend')
sys.path.insert(0, backend_path)

# Change to the backend directory
os.chdir(backend_path)

try:
    # Try to import the models individually to isolate the issue
    print("Testing individual model imports...")
    
    # Import dependencies first
    from sqlmodel import SQLModel, Field
    from typing import Optional
    from datetime import datetime
    
    print("Dependencies imported successfully")
    
    # Define a minimal model similar to what might be causing the issue
    from sqlmodel import SQLModel, Field
    from typing import Optional
    
    class TestModel(SQLModel, table=True):
        # This is how we expect fields to be defined
        id: Optional[int] = Field(default=None, primary_key=True)
        name: str = Field()
    
    print("Test model created successfully")
    
    # Now try to import the actual models
    print("\nTrying to import user model...")
    from src.models.user import User
    print("User model imported successfully")
    
    print("\nTrying to import todo model...")
    from src.models.todo import Todo
    print("Todo model imported successfully")
    
    print("\nTrying to import session model...")
    from src.models.session import Session
    print("Session model imported successfully")
    
    print("\nAll models imported successfully - no PydanticUserError found")
    
except Exception as e:
    print(f"\nError encountered: {type(e).__name__}: {e}")
    print("\nDetailed traceback:")
    traceback.print_exc()