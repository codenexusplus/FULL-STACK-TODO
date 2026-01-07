from sqlmodel import create_engine, Session as SQLModelSession, SQLModel
import os
from dotenv import load_dotenv

# 1. Force load the environment variables from .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# 2. Add a safety check to provide a better error message if .env is missing
if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL is None. Ensure your .env file exists in the /backend folder "
        "and contains DATABASE_URL=postgresql://..."
    )

# 3. Create the engine only after we are sure DATABASE_URL is a string
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,      # Verify connections before use
    pool_recycle=3600        # Recycle connections every hour
)

def create_db_and_tables():
    print("Creating database and tables...")
    try:
        # Import models to register them with SQLModel before creating tables
        from .models.user import User
        from .models.todo import Todo
        from .models.session import Session  # User session model
        SQLModel.metadata.create_all(engine)
        print("Database and tables created successfully.")
    except Exception as e:
        print(f"Error creating database and tables: {e}")

def get_session():
    with SQLModelSession(engine) as session:
        yield session