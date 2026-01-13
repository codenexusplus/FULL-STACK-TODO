import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlmodel import SQLModel, create_engine
from src.api import auth, todos
from src.models.user import User
from src.models.todo import Todo
from src.models.session import Session

# 1. Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 2. Load Environment Variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Safety Check
if not DATABASE_URL:
    logger.error("CRITICAL: DATABASE_URL not found. Check your environment variables.")
    raise ValueError("DATABASE_URL not found in environment variables")

# 3. Create Engine
engine = create_engine(DATABASE_URL)

app = FastAPI(title="Todo App API")

# 4. CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins for simplicity in Vercel
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
        content={"message": "Internal Server Error", "detail": str(exc)},
    )

# 6. Database Startup
@app.on_event("startup")
def on_startup():
    logger.info("Syncing Database Tables...")
    try:
        SQLModel.metadata.create_all(engine)
        logger.info("Database tables synced successfully.")
    except Exception as e:
        logger.error(f"Failed to sync database: {e}")

# 7. Routes
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(todos.router, prefix="/api/todos", tags=["todos"])

@app.get("/")
async def root():
    return {"status": "online"}

@app.get("/api")
async def api_root():
    return {"status": "online", "message": "Welcome to the API"}
