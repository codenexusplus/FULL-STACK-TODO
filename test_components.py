import sys
import os
from dotenv import load_dotenv

# Load environment variables
project_root = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(project_root, '.env')
load_dotenv(env_file_path)

# Add the backend directory to the Python path
backend_path = os.path.join(project_root, 'backend')
sys.path.insert(0, backend_path)

print("Testing database connection...")

try:
    from backend.src.database import engine
    print("✓ Database engine created successfully")
    
    # Test the connection
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
        print("✓ Database connection successful")
        
except Exception as e:
    print(f"✗ Database connection failed: {e}")
    import traceback
    traceback.print_exc()

print("\nTesting model imports...")
try:
    from backend.src.models.user import User
    print("✓ User model imported successfully")
except Exception as e:
    print(f"✗ Failed to import User model: {e}")
    import traceback
    traceback.print_exc()

try:
    from backend.src.models.todo import Todo, PriorityEnum
    print("✓ Todo model and PriorityEnum imported successfully")
except Exception as e:
    print(f"✗ Failed to import Todo model: {e}")
    import traceback
    traceback.print_exc()

print("\nTesting service imports...")
try:
    from backend.src.services.todo_service import get_todos
    print("✓ Todo service imported successfully")
except Exception as e:
    print(f"✗ Failed to import Todo service: {e}")
    import traceback
    traceback.print_exc()

print("\nTesting API router imports...")
try:
    from backend.src.api.todos import router
    print("✓ Todos API router imported successfully")
except Exception as e:
    print(f"✗ Failed to import Todos API router: {e}")
    import traceback
    traceback.print_exc()