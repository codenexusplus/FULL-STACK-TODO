#!/usr/bin/env python3
"""Test script to check if models import correctly"""

import sys
import traceback
sys.path.insert(0, '.')

try:
    print("Testing import of user model...")
    from src.models.user import User
    print("✓ User model imported successfully")
    
    print("Testing import of todo model...")
    from src.models.todo import Todo
    print("✓ Todo model imported successfully")
    
    print("Testing import of session model...")
    from src.models.session import Session
    print("✓ Session model imported successfully")
    
    print("\nAll models imported successfully!")
    
except Exception as e:
    print(f"✗ Error importing models: {e}")
    print("\nDetailed traceback:")
    traceback.print_exc()