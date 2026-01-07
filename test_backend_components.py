import os
import sys
from dotenv import load_dotenv

# Load environment variables from the project root
project_root = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(project_root, '.env')
load_dotenv(env_file_path)

# Add the project root to the Python path so imports work correctly
sys.path.insert(0, project_root)

print("Testing imports...")

try:
    # Test importing the main components
    from backend.src.api.todos import router
    print("✓ Todos API router imported successfully")
    
    from backend.src.services.todo_service import get_todos
    print("✓ Todo service imported successfully")
    
    from backend.src.auth_middleware import get_current_user
    print("✓ Auth middleware imported successfully")
    
    # Test database connection
    from backend.src.database import get_session
    print("✓ Database connection imported successfully")
    
    # Test with a real session
    print("Testing database session...")
    session_gen = get_session()
    session = next(session_gen)
    print("✓ Database session created successfully")
    
    # Close the session
    session.close()
    
    print("\nAll components are working correctly!")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()