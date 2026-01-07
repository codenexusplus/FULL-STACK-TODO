from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Annotated, List
from ..models.todo import Todo, TodoCreate, TodoRead, TodoUpdate
from ..services.todo_service import (
    create_todo, get_todos, get_todo_by_id, update_todo, delete_todo, toggle_todo_completion
)
from ..database import get_session
from ..auth_middleware import get_current_user
from ..models.user import User

router = APIRouter()


@router.get("/{user_id}/tasks", response_model=List[TodoRead])
def read_todos(
    user_id: int,
    session: Annotated[Session, Depends(get_session)],
    current_user: User = Depends(get_current_user)
):
    """
    Retrieve todos for the authenticated user.
    """
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to access these todos."
        )
    todos = get_todos(session, user_id)
    return todos


@router.post("/{user_id}/tasks", response_model=TodoRead)
def create_new_todo(
    user_id: int,
    todo: TodoCreate,
    session: Annotated[Session, Depends(get_session)],
    current_user: User = Depends(get_current_user)
):
    """
    Create a new todo for the authenticated user.
    """
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to create todos for this user."
        )
    db_todo = create_todo(session, todo, user_id)
    return db_todo


@router.get("/{user_id}/tasks/{id}", response_model=TodoRead)
def read_todo(
    user_id: int,
    id: int,
    session: Annotated[Session, Depends(get_session)],
    current_user: User = Depends(get_current_user)
):
    """
    Get a specific todo by ID for the authenticated user.
    """
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to access this todo."
        )
    db_todo = get_todo_by_id(session, id, user_id)
    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    return db_todo


@router.put("/{user_id}/tasks/{id}", response_model=TodoRead)
def update_existing_todo(
    user_id: int,
    id: int,
    todo_update: TodoUpdate,
    session: Annotated[Session, Depends(get_session)],
    current_user: User = Depends(get_current_user)
):
    """
    Update a specific todo by ID for the authenticated user.
    """
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to update this todo."
        )
    db_todo = update_todo(session, id, todo_update, user_id)
    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    return db_todo


@router.patch("/{user_id}/tasks/{id}/complete", response_model=TodoRead)
def toggle_complete_todo(
    user_id: int,
    id: int,
    session: Annotated[Session, Depends(get_session)],
    current_user: User = Depends(get_current_user)
):
    """
    Toggle the completion status of a specific todo by ID for the authenticated user.
    """
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to modify this todo."
        )
    db_todo = toggle_todo_completion(session, id, user_id)
    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    return db_todo


@router.delete("/{user_id}/tasks/{id}")
def delete_existing_todo(
    user_id: int,
    id: int,
    session: Annotated[Session, Depends(get_session)],
    current_user: User = Depends(get_current_user)
):
    """
    Delete a specific todo by ID for the authenticated user.
    """
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to delete this todo."
        )
    success = delete_todo(session, id, user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    return {"message": "Todo deleted successfully"}