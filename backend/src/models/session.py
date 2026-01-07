from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
from .user import User


class Session(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    token: str = Field(unique=True, index=True)  # JWT token
    user_id: int = Field(foreign_key="user.id")
    expires_at: datetime
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)

    # Relationship to User
    user: Optional[User] = Relationship()