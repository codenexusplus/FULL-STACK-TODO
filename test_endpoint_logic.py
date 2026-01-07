import os
import sys
from dotenv import load_dotenv

# Load environment variables from the project root
project_root = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(project_root, '.env')
load_dotenv(env_file_path)

# Add the project root to the Python path so imports work correctly
sys.path.insert(0, project_root)

# Test importing the necessary modules to check for import errors
try:
    from backend.src.database import get_session
    print("✓ Database module imported successfully")
except Exception as e:
    print(f"✗ Database module import failed: {e}")

try:
    from backend.src.auth_middleware import get_current_user
    print("✓ Auth middleware imported successfully")
except Exception as e:
    print(f"✗ Auth middleware import failed: {e}")

try:
    from backend.src.services.todo_service import get_todos
    print("✓ Todo service imported successfully")
except Exception as e:
    print(f"✗ Todo service import failed: {e}")

try:
    from backend.src.models.user import User
    print("✓ User model imported successfully")
except Exception as e:
    print(f"✗ User model import failed: {e}")

try:
    from backend.src.models.todo import Todo
    print("✓ Todo model imported successfully")
except Exception as e:
    print(f"✗ Todo model import failed: {e}")

# Test the database connection
try:
    print("\nTesting database connection...")
    with next(get_session()) as session:
        print("✓ Database connection successful")
        
        # Test if we can query users
        from sqlmodel import select
        result = session.exec(select(User).limit(1))
        user = result.first()
        print(f"✓ User query successful, found user: {user is not None}")
        
        # Test if we can query todos for user ID 1
        result = session.exec(select(Todo).where(Todo.user_id == 1).limit(5))
        todos = result.all()
        print(f"✓ Todo query for user_id=1 successful, found {len(todos)} todos")
        
except Exception as e:
    print(f"✗ Database test failed: {e}")
    import traceback
    traceback.print_exc()