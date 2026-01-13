# backend_server.py
import uvicorn
import os
import sys

if __name__ == "__main__":
    # Check if we're already in the backend directory
    if os.path.exists('.env') and os.path.exists('src'):
        # We're already in the backend directory
        current_dir = os.getcwd()
        print(f"Running from directory: {current_dir}")
    else:
        # Change directory to the 'backend' folder so that all relative paths in the app work correctly
        # (e.g., loading the .env file)
        backend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend')
        if os.path.exists(backend_dir):
            os.chdir(backend_dir)
            print(f"Changed to backend directory: {os.getcwd()}")
        else:
            print("Backend directory not found. Exiting.")
            sys.exit(1)

    # Run the uvicorn server
    # --reload will watch for file changes and restart the server
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8002,
        reload=True,
        log_level="info"
    )
