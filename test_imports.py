import os
import sys
import traceback

print("Testing individual imports...")

# Load environment variables from the project root
project_root = os.path.dirname(os.path.abspath(__file__))
print(f"Project root: {project_root}")

# Add both the project root and the backend directory to the Python path
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, 'backend'))

print("Added paths to sys.path")

# Test each import individually
try:
    print("Testing: from backend.src.api import auth, todos")
    from backend.src.api import auth, todos
    print("SUCCESS: Imported auth and todos")
except Exception as e:
    print(f"ERROR importing auth, todos: {e}")
    traceback.print_exc()

try:
    print("Testing: from backend.src.database import create_db_and_tables")
    from backend.src.database import create_db_and_tables
    print("SUCCESS: Imported database functions")
except Exception as e:
    print(f"ERROR importing database functions: {e}")
    traceback.print_exc()

try:
    print("Testing: Creating FastAPI app")
    from fastapi import FastAPI
    app = FastAPI()
    print("SUCCESS: Created FastAPI app")
except Exception as e:
    print(f"ERROR creating FastAPI app: {e}")
    traceback.print_exc()

try:
    print("Testing: Adding CORS middleware")
    from fastapi.middleware.cors import CORSMiddleware
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    print("SUCCESS: Added CORS middleware")
except Exception as e:
    print(f"ERROR adding CORS middleware: {e}")
    traceback.print_exc()

try:
    print("Testing: Including routers")
    app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
    app.include_router(todos.router, prefix="/api/todos", tags=["todos"])
    print("SUCCESS: Included routers")
except Exception as e:
    print(f"ERROR including routers: {e}")
    traceback.print_exc()

print("All tests completed!")