#!/usr/bin/env python3
"""
Test script to check if a user exists in the database
"""
import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from src.database import engine
from src.models.user import User
from sqlmodel import Session, select

def check_users():
    print("Connecting to database...")
    
    with Session(engine) as session:
        print("Connected to database, fetching users...")
        
        statement = select(User)
        users = session.exec(statement).all()
        
        print(f"Found {len(users)} users in database:")
        for user in users:
            print(f"  - Email: {user.email}, ID: {user.id}, Name: {user.name}")
        
        # Check specifically for misscode110@gmail.com
        target_user = session.exec(select(User).where(User.email == "misscode110@gmail.com")).first()
        if target_user:
            print(f"\nTarget user found: {target_user.email}")
        else:
            print(f"\nTarget user NOT found: misscode110@gmail.com")

if __name__ == "__main__":
    check_users()