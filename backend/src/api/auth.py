from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel

from ..models.user import User, UserCreate, UserRead
from ..models.session import SessionModel
from ..services.user_service import create_user, get_user_by_email, authenticate_user
from ..database import get_session
from ..auth import create_access_token
from ..core.config import settings
from ..auth_middleware import get_current_user

router = APIRouter()

class EmailSignInRequest(BaseModel):
    username: str
    password: str

@router.post("/sign-up/email", response_model=UserRead)
async def sign_up(
    user_create: UserCreate,
    session: Annotated[Session, Depends(get_session)]
):
    try:
        db_user = get_user_by_email(session, user_create.email)
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        return create_user(session, user_create)
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        from ..main import logger
        logger.error(f"Error in sign-up: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Registration failed"
        )

@router.post("/sign-in/email")
async def sign_in(
    request: Request,
    session: Annotated[Session, Depends(get_session)]
):
    try:
        # Log incoming request for debugging
        from ..main import logger
        logger.info(f"Sign-in request received with headers: {dict(request.headers)}")

        # Try to parse as JSON first (for API clients)
        content_type = request.headers.get("Content-Type", "").lower()
        username = None
        password = None

        if "application/json" in content_type:
            try:
                json_data = await request.json()
                username = json_data.get("username") or json_data.get("email")
                password = json_data.get("password")
                logger.info(f"Parsed JSON data - username: {username}, has_password: {password is not None}")
            except Exception as e:
                logger.error(f"Error parsing JSON: {str(e)}")
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid JSON format"
                )
        else:
            # Fall back to form data (for browser forms)
            try:
                form = await request.form()
                username = form.get("username") or form.get("email")
                password = form.get("password")
                logger.info(f"Parsed form data - username: {username}, has_password: {password is not None}")
            except Exception as e:
                logger.error(f"Error parsing form data: {str(e)}")
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid form data"
                )

        # Validate inputs
        if not username or not password:
            logger.error(f"Missing credentials - username: {username is not None}, password: {password is not None}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username and password are required"
            )

        # Sanitize inputs to prevent injection attacks
        username = str(username).strip()
        password = str(password).strip()

        logger.info(f"Attempting to authenticate user: {username}")

        # Attempt authentication - wrap in try-catch to prevent 500 errors
        try:
            user = authenticate_user(session, username, password)
        except Exception as e:
            logger.error(f"Error during authentication: {str(e)}", exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Authentication service temporarily unavailable"
            )

        if not user:
            logger.warning(f"Authentication failed for user: {username} - user not found or invalid password")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        logger.info(f"Authentication successful for user: {user.email}")

        access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)

        # Create access token - wrap in try-catch to prevent 500 errors
        try:
            access_token = create_access_token(
                data={"sub": user.email, "user_id": user.id}, expires_delta=access_token_expires
            )
        except Exception as e:
            logger.error(f"Error creating access token: {str(e)}", exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Token generation failed"
            )

        logger.info(f"Access token created for user: {user.email}")

        # Create a session record - wrap in try-catch to prevent 500 errors
        try:
            session_record = SessionModel(
                token=access_token,
                user_id=user.id,
                expires_at=datetime.utcnow() + access_token_expires
            )
            session.add(session_record)
            session.commit()
            session.refresh(session_record)  # Refresh to get the ID of the created session
        except Exception as e:
            logger.error(f"Error creating session record: {str(e)}", exc_info=True)
            # Don't raise an exception here as the user is authenticated, just log it
            pass

        logger.info(f"Session record created for user: {user.email}")

        # Ensure CORS headers are present in the response
        response = {"access_token": access_token, "token_type": "bearer"}

        # Return with proper CORS headers
        from fastapi.responses import JSONResponse
        return JSONResponse(
            content=response,
            headers={
                "Access-Control-Allow-Origin": request.headers.get("Origin", ""),
                "Access-Control-Allow-Credentials": "true",
                "Access-Control-Allow-Headers": request.headers.get("Access-Control-Request-Headers", "*"),
            }
        )
    except HTTPException as http_exc:
        # Re-raise HTTP exceptions as-is
        from ..main import logger
        logger.error(f"HTTP Exception in sign-in: {http_exc.detail}")
        # Ensure CORS headers are present even for error responses
        from fastapi.responses import JSONResponse
        return JSONResponse(
            content={"detail": http_exc.detail},
            status_code=http_exc.status_code,
            headers={
                "Access-Control-Allow-Origin": request.headers.get("Origin", ""),
                "Access-Control-Allow-Credentials": "true",
            }
        )
    except Exception as e:
        # Log the error for debugging
        from ..main import logger
        logger.error(f"Unexpected sign-in error: {str(e)}", exc_info=True)
        # Ensure CORS headers are present even for error responses
        from fastapi.responses import JSONResponse
        return JSONResponse(
            content={"detail": "Authentication failed"},
            status_code=500,
            headers={
                "Access-Control-Allow-Origin": request.headers.get("Origin", ""),
                "Access-Control-Allow-Credentials": "true",
            }
        )

@router.get("/me", response_model=UserRead)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.post("/sign-out")
async def sign_out(
    request: Request,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    try:
        # Extract token from the Authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authorization header missing or invalid"
            )

        token = auth_header.split(" ")[1]

        # Find the session by token
        from sqlalchemy import select
        session_record = session.exec(
            select(SessionModel).where(
                SessionModel.user_id == current_user.id,
                SessionModel.token == token,
                SessionModel.is_active == True
            )
        ).first()

        if session_record:
            session_record.is_active = False
            session.add(session_record)
            session.commit()

        return {"message": "Successfully logged out"}
    except HTTPException:
        raise
    except Exception as e:
        from ..main import logger
        logger.error(f"Error in sign-out: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Sign out failed"
        )
