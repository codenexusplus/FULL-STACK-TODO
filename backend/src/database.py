from sqlmodel import create_engine, Session as SQLModelSession, SQLModel
from .core.config import settings

# Create the engine using the centralized settings
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False  # Set to True to see SQL queries
)

def get_session():
    with SQLModelSession(engine) as session:
        yield session

def create_db_and_tables():
    """
    Initializes the database by creating all tables defined by SQLModel models.
    This function should be called from a controlled script, not from a startup event,
    to avoid issues with auto-reloaders causing duplicate table definitions.
    """
    # Import all models here so they are registered with SQLModel's metadata
    from .models import user, todo, session
    
    print("Attempting to create database tables...")
    try:
        SQLModel.metadata.create_all(engine)
        print("Database tables created successfully (if they didn't exist).")
    except Exception as e:
        print(f"An error occurred during table creation: {e}")
