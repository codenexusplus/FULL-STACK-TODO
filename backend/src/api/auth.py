from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from typing import Annotated
from datetime import datetime

from ..models.user import User, UserCreate, UserRead
from ..models.session import Session as SessionModel
from ..services.user_service import create_user, get_user_by_email, authenticate_user
from ..database import get_session
from ..auth import create_access_token
from ..core.config import settings
from ..auth_middleware import get_current_user

router = APIRouter()

@router.post("/sign-up/email", response_model=UserRead)
async def sign_up(
    user_create: UserCreate,
    session: Annotated[Session, Depends(get_session)]
):
    db_user = get_user_by_email(session, user_create.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    return create_user(session, user_create)

@router.post("/sign-in/email")
async def sign_in(
    request: Request,
    session: Annotated[Session, Depends(get_session)]
):
    # Manually parse form data
    form = await request.form()
    username = form.get("username")
    password = form.get("password")

    user = authenticate_user(session, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.email, "user_id": user.id}, expires_delta=access_token_expires
    )

    # Create a session record
    session_record = SessionModel(
        token=access_token,
        user_id=user.id,
        expires_at=datetime.utcnow() + access_token_expires
    )
    session.add(session_record)
    session.commit()

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserRead)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.post("/sign-out")
async def sign_out(
    request: Request,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
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
