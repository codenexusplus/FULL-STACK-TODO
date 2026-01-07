import os
import sys
from dotenv import load_dotenv

# Load environment variables from the project root
project_root = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(project_root, '.env')
load_dotenv(env_file_path)

# Add the project root to the Python path so imports work correctly
sys.path.insert(0, project_root)

print("Testing database connection...")

try:
    # Import the database module
    from backend.src.database import engine
    print("Database engine imported successfully")
    
    # Test the connection
    with engine.connect() as conn:
        print("Database connection successful!")
        result = conn.execute("SELECT 1")
        print(f"Test query result: {result.fetchone()}")
        
    print("Database connection test completed successfully!")
    
except Exception as e:
    print(f"Database connection test failed: {e}")
    import traceback
    traceback.print_exc()