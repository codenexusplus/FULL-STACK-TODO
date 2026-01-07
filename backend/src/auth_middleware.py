from datetime import datetime
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from sqlmodel import Session
from typing import Generator
from .core.config import settings
from .models.user import User
from .database import get_session
from .services.user_service import get_user_by_email

security = HTTPBearer()


def get_current_user(
    token: HTTPAuthorizationCredentials = Depends(security),
    session: Session = Depends(get_session)
) -> User:
    """Get the current authenticated user from the JWT token.

    Args:
        token: The HTTP authorization credentials containing the JWT token
        session: The database session for querying user data

    Returns:
        User: The authenticated user object

    Raises:
        HTTPException: If the token is invalid, expired, or the user doesn't exist
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Use the api_secret_key from settings to decode the token (consistent with token creation)
        payload = jwt.decode(token.credentials, settings.api_secret_key, algorithms=[settings.algorithm])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # Fetch the user from the database
    user = get_user_by_email(session, email=email)
    if user is None:
        raise credentials_exception
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user"
        )

    return user