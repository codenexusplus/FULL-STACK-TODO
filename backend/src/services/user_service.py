from sqlmodel import Session, select
from typing import Optional
from ..models.user import User, UserCreate
from passlib.context import CryptContext

# Using a more compatible bcrypt scheme
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user_by_email(session: Session, email: str) -> Optional[User]:
    statement = select(User).where(User.email == email)
    user = session.exec(statement).first()
    return user


def create_user(session: Session, user_create: UserCreate) -> User:
    hashed_password = pwd_context.hash(user_create.password)
    db_user = User(
        email=user_create.email,
        name=user_create.name,
        hashed_password=hashed_password
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def authenticate_user(session: Session, email: str, password: str) -> Optional[User]:
    user = get_user_by_email(session, email)
    if not user:
        return None
    if not pwd_context.verify(password, user.hashed_password):
        return None
    return user