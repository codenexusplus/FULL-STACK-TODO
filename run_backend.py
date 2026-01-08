import os
import sys
import threading
import time
from dotenv import load_dotenv

# Load environment variables from the project root
project_root = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(project_root, '.env')
load_dotenv(env_file_path)

# Add both the project root and the backend directory to the Python path
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, 'backend'))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the API routers using absolute imports
from backend.src.api import auth, todos
from backend.src.database import create_db_and_tables

app = FastAPI()

# This unblocks the connection between frontend and backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Local Next.js development
        "http://localhost:3001",  # Alternative local Next.js port
        "https://*.vercel.app",   # Vercel deployments
        "http://localhost:8002",  # Allow backend to backend requests
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables on startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(todos.router, prefix="/api/todos", tags=["todos"])

@app.get("/")
async def root():
    return {"message": "Backend is active and CORS is unblocked"}

def run_server():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8002, log_level="info")

if __name__ == "__main__":
    print("Starting server in a thread...")
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    
    print("Server thread started. Waiting for it to initialize...")
    time.sleep(2)  # Give the server some time to start
    
    print("Server should now be running on http://localhost:8002/")
    
    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down server...")
        sys.exit(0)