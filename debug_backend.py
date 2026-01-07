import os
import sys
from dotenv import load_dotenv

# Load environment variables from the project root
project_root = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(project_root, '.env')
load_dotenv(env_file_path)

# Add the project root to the Python path so imports work correctly
sys.path.insert(0, project_root)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

# Set up logging to see detailed errors
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Import the API routers using absolute imports
from backend.src.api import auth, todos

app = FastAPI()

# This unblocks the connection between Port 3000 and Port 8002
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(todos.router, prefix="/api/todos", tags=["todos"])

@app.get("/")
async def root():
    return {"message": "Backend is active and CORS is unblocked"}

@app.get("/test-db")
async def test_db():
    try:
        from backend.src.database import get_session
        from sqlmodel import select
        from backend.src.models.user import User
        
        # Test database connection
        with next(get_session()) as session:
            result = session.exec(select(User).limit(1))
            user = result.first()
            return {"status": "success", "user_found": user is not None}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002, log_level="debug", reload=False)