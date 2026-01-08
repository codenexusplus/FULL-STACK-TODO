import os
import sys
import traceback
from dotenv import load_dotenv

print("Starting backend with error handling...")

try:
    # Load environment variables from the project root
    project_root = os.path.dirname(os.path.abspath(__file__))
    env_file_path = os.path.join(project_root, '.env')
    load_dotenv(env_file_path)

    print(f"Loaded environment variables from: {env_file_path}")

    # Add both the project root and the backend directory to the Python path
    sys.path.insert(0, project_root)
    sys.path.insert(0, os.path.join(project_root, 'backend'))

    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware

    # Import the API routers using absolute imports
    from backend.src.api import auth, todos
    from backend.src.database import create_db_and_tables

    app = FastAPI()

    # This unblocks the connection between Port 3000 and Port 8002
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
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

    print("App created successfully. Starting server...")

    if __name__ == "__main__":
        import uvicorn
        print("About to start uvicorn server...")
        uvicorn.run(app, host="127.0.0.1", port=8003, reload=False)
        print("Server started on port 8003")

except Exception as e:
    print(f"Error occurred: {e}")
    traceback.print_exc()