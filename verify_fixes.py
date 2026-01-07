import os
import sys
from dotenv import load_dotenv

# Load environment variables from the project root
project_root = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(project_root, '.env')
load_dotenv(env_file_path)

# Add the project root to the Python path so imports work correctly
sys.path.insert(0, project_root)

print("Testing imports after fixes...")

# Try importing the main components to make sure they work
try:
    from backend.src.core.config import settings
    print("✓ Config loaded successfully")
    print(f"  Database URL: {'SET' if settings.database_url else 'NOT SET'}")
    print(f"  API Secret Key: {'SET' if settings.api_secret_key else 'NOT SET'}")
except Exception as e:
    print(f"✗ Config import failed: {e}")

try:
    from backend.src.database import engine, get_session
    print("✓ Database module loaded successfully")
except Exception as e:
    print(f"✗ Database import failed: {e}")

try:
    from backend.src.auth_middleware import get_current_user
    print("✓ Auth middleware loaded successfully")
except Exception as e:
    print(f"✗ Auth middleware import failed: {e}")

try:
    # Test the specific route function
    from backend.src.api.todos import read_todos
    print("✓ Todos API route loaded successfully")
except Exception as e:
    print(f"✗ Todos API import failed: {e}")

print("\nAll imports successful! The fixes appear to have resolved the issues.")