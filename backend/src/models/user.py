from __future__ import annotations

from sqlmodel import SQLModel, Field
from pydantic import BaseModel, field_validator, ConfigDict
from typing import Optional
from datetime import datetime


class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    name: str
    hashed_password: str
    is_active: bool = Field(default=True)
    email_verified: bool = Field(default=False)
    image: Optional[str] = Field(default=None)


class User(UserBase, table=True):
    __tablename__ = "user"

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UserCreate(BaseModel):
    email: str
    name: str
    password: str

    @field_validator("password")
    @classmethod
    def validate_password_length(cls, v: str) -> str:
        if len(v) > 72:
            raise ValueError("Password must not exceed 72 characters")
        return v


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    name: str
    email_verified: bool
    is_active: bool
    image: Optional[str] = None
    created_at: datetime
