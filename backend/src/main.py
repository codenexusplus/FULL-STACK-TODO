import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .database import create_db_and_tables
from .api import auth, todos

# 1. Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get settings
from .core.config import settings

app = FastAPI(title="Todo App API")

# 4. CORS Middleware
# Origins should be a list of strings
origins = [
    "http://localhost:3000", # Local frontend
]

# If a specific frontend URL is configured in settings, add it
if settings.next_public_api_base_url:
    # The setting is named "...api_base_url", but it's for the frontend client.
    # Let's clean it up to avoid confusion. Assume it's the frontend URL.
    frontend_url = settings.next_public_api_base_url.rstrip('/')
    if frontend_url not in origins:
        origins.append(frontend_url)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 5. Global Error Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"GLOBAL ERROR: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error", "detail": str(exc)}
    )

# 7. Routes
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(todos.router, prefix="/api/todos", tags=["todos"])

@app.get("/")
async def root():
    return {"status": "online"}

