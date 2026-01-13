import uvicorn
from src.core.config import settings
import re

# Extract port from the API base URL setting
api_url = settings.next_public_api_base_url
# Default to port 8002 if parsing fails
default_port = 8002

# Use regex to extract the port from the URL
match = re.search(r':(\d+)$', api_url)
port = int(match.group(1)) if match else default_port

print(f"Starting server on port {port} based on API URL setting ({api_url})...")

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=port,
        reload=False,
        log_level="info"
    )