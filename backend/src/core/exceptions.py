from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging

logger = logging.getLogger(__name__)


class TodoAppException(Exception):
    """Base exception class for the Todo App"""
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class AuthenticationError(TodoAppException):
    """Raised when authentication fails"""
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message, 401)


class AuthorizationError(TodoAppException):
    """Raised when authorization fails"""
    def __init__(self, message: str = "Authorization failed"):
        super().__init__(message, 403)


class ValidationError(TodoAppException):
    """Raised when validation fails"""
    def __init__(self, message: str = "Validation failed"):
        super().__init__(message, 422)


class ResourceNotFoundError(TodoAppException):
    """Raised when a requested resource is not found"""
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, 404)


def add_exception_handlers(app: FastAPI):
    """Add exception handlers to the FastAPI app"""
    
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        logger.error(f"HTTP Exception: {exc.status_code} - {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": str(exc.detail), "status_code": exc.status_code}
        )
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logger.error(f"Validation Error: {exc.errors()}")
        return JSONResponse(
            status_code=422,
            content={
                "message": "Validation failed",
                "errors": exc.errors(),
                "status_code": 422
            }
        )
    
    @app.exception_handler(TodoAppException)
    async def todo_app_exception_handler(request: Request, exc: TodoAppException):
        logger.error(f"Todo App Exception: {exc.status_code} - {exc.message}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.message, "status_code": exc.status_code}
        )
    
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        logger.error(f"General Exception: {str(exc)}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={"message": "Internal server error", "status_code": 500}
        )