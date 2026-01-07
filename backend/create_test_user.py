#!/usr/bin/env python3
"""
Script to create a test user in the database
"""
import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from src.database import get_session
from src.models.user import UserCreate
from src.services.user_service import create_user
from sqlmodel import Session

def create_test_user():
    print("Creating a test user...")

    # Use the email from the error message
    email = "misscode110@gmail.com"
    name = "Miss Code"
    password = "123"  # Using a very short password for testing

    # Create the user
    with Session(get_session().__next__().bind) as session:
        user_create = UserCreate(email=email, name=name, password=password)
        try:
            user = create_user(session, user_create)
            print(f"User created successfully! ID: {user.id}, Email: {user.email}")
        except Exception as e:
            print(f"Error creating user: {e}")

if __name__ == "__main__":
    create_test_user()