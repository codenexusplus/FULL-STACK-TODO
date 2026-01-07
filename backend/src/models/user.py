from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel, field_validator
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

# Prevent circular imports
if TYPE_CHECKING:
    from .todo import Todo

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    name: str
    hashed_password: str
    is_active: bool = Field(default=True)
    email_verified: bool = Field(default=False)
    image: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Pydantic models for API requests/responses
class UserCreate(BaseModel):
    email: str
    name: str
    password: str

    @field_validator('password')
    @classmethod
    def validate_password_length(cls, v):
        if len(v) > 72:
            raise ValueError('Password must not exceed 72 characters due to bcrypt limitations')
        return v

class UserRead(BaseModel):
    id: int
    email: str
    name: str
    email_verified: bool
    is_active: bool
    image: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True