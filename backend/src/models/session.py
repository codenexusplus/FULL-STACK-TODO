from __future__ import annotations

from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime

# Circular import se bachne ke liye
if TYPE_CHECKING:
    from .user import User


class SessionModel(SQLModel, table=True):
    __tablename__ = "session"

    id: Optional[int] = Field(default=None, primary_key=True)
    token: str = Field(unique=True, index=True)
    user_id: int = Field(foreign_key="user.id")
    expires_at: datetime
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)

    # Fixed SQLModel relationship to avoid SQLAlchemy error
    user: User = Relationship()
