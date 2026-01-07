#!/usr/bin/env python3
"""
Script to test login with known credentials
"""
import sys
import os
import requests

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

def test_login():
    # API base URL - adjust as needed
    api_url = "http://localhost:8002/api/auth/sign-in/email"
    
    # Known credentials
    credentials = {
        "username": "misscode110@gmail.com",  # The email without space that's in the DB
        "password": "123"  # The password used during registration
    }
    
    print(f"Attempting to login with email: {credentials['username']}")
    
    try:
        # Create form data as the backend expects
        import requests
        response = requests.post(api_url, data=credentials)
        
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")
        
        if response.status_code == 200:
            print("Login successful!")
            return True
        else:
            print("Login failed!")
            return False
            
    except Exception as e:
        print(f"Error during login attempt: {e}")
        return False

if __name__ == "__main__":
    test_login()