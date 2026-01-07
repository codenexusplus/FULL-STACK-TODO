import os
import sys
from dotenv import load_dotenv

# Load environment variables from the project root
project_root = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(project_root, '.env')
load_dotenv(env_file_path)

# Add the project root to the Python path so imports work correctly
sys.path.insert(0, project_root)

try:
    # Import the database engine and create tables if they don't exist
    from backend.src.database import engine, create_db_and_tables
    print("Creating database tables if they don't exist...")
    create_db_and_tables()
    print("Database tables created successfully!")
    
    # Test the database connection
    from backend.src.database import get_session
    from sqlmodel import select
    from backend.src.models.user import User
    
    print("Testing database connection...")
    with next(get_session()) as session:
        # Try to query for a user with ID 1
        statement = select(User).where(User.id == 1)
        user = session.exec(statement).first()
        print(f"User with ID 1 exists: {user is not None}")
        
        if user:
            print(f"User email: {user.email}")
            print(f"User name: {user.name}")
            print(f"User is active: {user.is_active}")
        
        print("Database connection test completed successfully!")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()