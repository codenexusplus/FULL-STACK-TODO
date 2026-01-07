from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from sqlalchemy import Column

if TYPE_CHECKING:
    from .user import User

# In classes ko rehne dein taake baqi files crash na hon
class PriorityEnum:
    high = "High"
    medium = "Medium"
    low = "Low"

class CategoryEnum:
    work = "Work"
    life = "Life"
    urgent = "Urgent"

class TodoBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    is_completed: bool = Field(default=False)
    priority: str = Field(default="Medium")
    category: str = Field(default="Life")
    due_date: Optional[datetime] = Field(default=None)
    estimated_minutes: Optional[int] = Field(default=None, ge=1)
    recurring_interval: str = Field(default="None")

class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # updated_at automatically update hone ke liye
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(
            "updated_at",
            default=datetime.utcnow,
            onupdate=datetime.utcnow
        )
    )

    # RELATIONSHIP
    user: Optional["User"] = Relationship()

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime
    user_id: int

class TodoUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    priority: Optional[str] = None
    category: Optional[str] = None
    due_date: Optional[datetime] = None
    estimated_minutes: Optional[int] = None
    recurring_interval: Optional[str] = None