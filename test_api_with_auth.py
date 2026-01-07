import requests
import json
import urllib3
from datetime import datetime, timedelta
from jose import JWTError, jwt

# Disable SSL warnings for local testing
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Test the backend API
BASE_URL = "http://localhost:8002"

def create_test_token():
    """Create a test JWT token for testing purposes"""
    # Note: This is for testing only - in production, tokens are created during login
    from backend.src.core.config import settings
    
    # Create a mock user payload
    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode = {
        "sub": "test@example.com",  # Mock email
        "exp": expire.timestamp(),
        "user_id": 1  # Mock user ID
    }
    
    encoded_jwt = jwt.encode(to_encode, settings.api_secret_key, algorithm=settings.algorithm)
    return encoded_jwt

def test_api_with_auth():
    print("Testing the backend API with authentication...")
    
    # Create a test token
    try:
        token = create_test_token()
        print(f"Created test token: {token[:20]}...")
    except Exception as e:
        print(f"Error creating test token: {e}")
        # If we can't create a token, try to register/login a user first
        return
    
    # Test the todos endpoint with the token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(f"{BASE_URL}/api/todos/1/tasks", headers=headers, verify=False)
        print(f"Todos endpoint: {response.status_code}")
        if response.status_code == 200:
            print(f"Success: {response.json()}")
        elif response.status_code == 404:
            print(f"No tasks found (which is OK): {response.text}")
        else:
            print(f"Error response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error connecting to todos endpoint: {e}")
        import traceback
        traceback.print_exc()

def test_api_without_auth():
    print("\nTesting the backend API without authentication (should fail)...")
    
    # Test the todos endpoint without auth (should fail)
    try:
        response = requests.get(f"{BASE_URL}/api/todos/1/tasks", verify=False)
        print(f"Todos endpoint without auth: {response.status_code}")
        if response.status_code == 401:
            print("Expected: Unauthorized (401) - authentication required")
        else:
            print(f"Unexpected response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error connecting to todos endpoint: {e}")
        import traceback
        traceback.print_exc()

def test_root_endpoint():
    print("\nTesting the root endpoint...")
    
    try:
        response = requests.get(f"{BASE_URL}/", verify=False)
        print(f"Root endpoint: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"Error connecting to root endpoint: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_root_endpoint()
    test_api_without_auth()
    test_api_with_auth()