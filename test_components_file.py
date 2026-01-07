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

results = []

results.append("Testing database connection...")

try:
    from backend.src.database import engine
    results.append("✓ Database engine created successfully")
    
    # Test the connection
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
        results.append("✓ Database connection successful")
        
except Exception as e:
    results.append(f"✗ Database connection failed: {e}")
    import traceback
    import io
    sio = io.StringIO()
    traceback.print_exc(file=sio)
    results.append(sio.getvalue())

results.append("\nTesting model imports...")
try:
    from backend.src.models.user import User
    results.append("✓ User model imported successfully")
except Exception as e:
    results.append(f"✗ Failed to import User model: {e}")
    import traceback
    import io
    sio = io.StringIO()
    traceback.print_exc(file=sio)
    results.append(sio.getvalue())

try:
    from backend.src.models.todo import Todo, PriorityEnum
    results.append("✓ Todo model and PriorityEnum imported successfully")
except Exception as e:
    results.append(f"✗ Failed to import Todo model: {e}")
    import traceback
    import io
    sio = io.StringIO()
    traceback.print_exc(file=sio)
    results.append(sio.getvalue())

results.append("\nTesting service imports...")
try:
    from backend.src.services.todo_service import get_todos
    results.append("✓ Todo service imported successfully")
except Exception as e:
    results.append(f"✗ Failed to import Todo service: {e}")
    import traceback
    import io
    sio = io.StringIO()
    traceback.print_exc(file=sio)
    results.append(sio.getvalue())

results.append("\nTesting API router imports...")
try:
    from backend.src.api.todos import router
    results.append("✓ Todos API router imported successfully")
except Exception as e:
    results.append(f"✗ Failed to import Todos API router: {e}")
    import traceback
    import io
    sio = io.StringIO()
    traceback.print_exc(file=sio)
    results.append(sio.getvalue())

# Write results to a file
with open("test_results.txt", "w") as f:
    for result in results:
        f.write(result + "\n")
        f.write("-" * 50 + "\n")

print("Test completed. Results written to test_results.txt")