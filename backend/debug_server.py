import uvicorn
import logging

# Set up logging to see more details
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    print("Starting server on port 8003...")
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8003,
        reload=False,
        log_level="debug"
    )