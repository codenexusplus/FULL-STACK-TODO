import requests
import json
import urllib3

# Disable SSL warnings for local testing
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Test the backend API
BASE_URL = "http://localhost:8002"

def test_api():
    print("Testing the backend API...")

    # Test the root endpoint
    try:
        response = requests.get(f"{BASE_URL}/", verify=False)
        print(f"Root endpoint: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"Error connecting to root endpoint: {e}")
        import traceback
        traceback.print_exc()

    # Test the todos endpoint (this will likely fail without auth)
    try:
        response = requests.get(f"{BASE_URL}/api/todos/1/tasks", verify=False)
        print(f"Todos endpoint: {response.status_code}")
        if response.status_code == 401 or response.status_code == 403:
            print("Expected: Unauthorized access (need JWT token)")
        elif response.status_code == 200:
            print(f"Success: {response.json()}")
        else:
            print(f"Other response: {response.text}")
    except Exception as e:
        print(f"Error connecting to todos endpoint: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_api()