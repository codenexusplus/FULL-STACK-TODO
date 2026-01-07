import os
import sys
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session, select
from passlib.context import CryptContext

# Load environment variables from the project root
project_root = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(project_root, '.env')
load_dotenv(env_file_path)

# Add the project root to the Python path so imports work correctly
sys.path.insert(0, project_root)

# Initialize password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_sample_user():
    try:
        # Import models
        from backend.src.models.user import User
        from backend.src.database import engine, create_db_and_tables
        
        # Create tables
        create_db_and_tables()
        
        # Create a sample user with ID 1
        with Session(engine) as session:
            # Check if user with ID 1 already exists
            existing_user = session.get(User, 1)
            if existing_user:
                print(f"User with ID 1 already exists: {existing_user.email}")
                return
            
            # Create a sample user
            hashed_password = pwd_context.hash("password123")  # Default password
            sample_user = User(
                id=1,
                email="user@example.com",
                name="Sample User",
                hashed_password=hashed_password,
                is_active=True,
                email_verified=True
            )
            
            session.add(sample_user)
            session.commit()
            session.refresh(sample_user)
            
            print(f"Created sample user with ID 1: {sample_user.email}")
    
    except Exception as e:
        print(f"Error creating sample user: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    create_sample_user()