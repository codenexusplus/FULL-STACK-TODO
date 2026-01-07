import os
import sys
from dotenv import load_dotenv

# Load environment variables first
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_file_path = os.path.join(project_root, '.env')
load_dotenv(env_file_path)

# Add the src directory to the Python path
src_path = os.path.join(project_root, 'backend', 'src')
sys.path.insert(0, src_path)

# Now import and reload the config module to ensure it uses the environment variables
import importlib
from core import config
importlib.reload(config)

# Now continue with the rest of the imports
import logging
from fastapi import FastAPI
from api import auth, todos
from database import engine
from models import user, todo  # Import models to register them with SQLModel
from core.logging_config import setup_logging
from core.exceptions import add_exception_handlers
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

# Set up logging
setup_logging()

# Create the FastAPI app
app = FastAPI(title="Todo App API", version="1.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

# Add exception handlers
add_exception_handlers(app)

# Include the API routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(todos.router, prefix="/api/todos", tags=["todos"])


@app.on_event("startup")
def on_startup():
    # Create database tables
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(bind=engine)
    logging.info("Database tables created successfully")


@app.get("/")
def read_root():
    logging.info("Root endpoint accessed")
    return {"message": "Welcome to the Todo App API"}

@app.get("/favicon.ico", include_in_schema=False)
async def get_favicon():
    return RedirectResponse(url="/static/favicon.ico")