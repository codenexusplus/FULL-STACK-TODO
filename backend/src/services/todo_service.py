from sqlmodel import Session, select
from typing import Optional
from ..models.todo import Todo, TodoCreate, TodoUpdate, PriorityEnum
from ..models.user import User


def create_todo(session: Session, todo: TodoCreate, user_id: int) -> Todo:
    """Create a new todo item for a specific user.

    Args:
        session: The database session
        todo: The todo data to create
        user_id: The ID of the user who owns this todo

    Returns:
        Todo: The created todo object with ID and timestamps
    """
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        is_completed=todo.is_completed,
        user_id=user_id
    )
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


def get_todos(session: Session, user_id: int) -> list[Todo]:
    """Get all todos for a specific user.

    Args:
        session: The database session
        user_id: The ID of the user whose todos to retrieve

    Returns:
        list[Todo]: A list of todos belonging to the user
    """
    statement = select(Todo).where(Todo.user_id == user_id)
    todos = session.exec(statement).all()
    return todos


def get_todo_by_id(session: Session, todo_id: int, user_id: int) -> Optional[Todo]:
    """Get a specific todo by ID for a specific user.

    Args:
        session: The database session
        todo_id: The ID of the todo to retrieve
        user_id: The ID of the user who owns this todo

    Returns:
        Todo: The todo object if found, None otherwise
    """
    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
    todo = session.exec(statement).first()
    return todo


def update_todo(session: Session, todo_id: int, todo_update: TodoUpdate, user_id: int) -> Optional[Todo]:
    """Update a specific todo by ID for a specific user.

    Args:
        session: The database session
        todo_id: The ID of the todo to update
        todo_update: The updated todo data
        user_id: The ID of the user who owns this todo

    Returns:
        Todo: The updated todo object if successful, None if not found
    """
    db_todo = get_todo_by_id(session, todo_id, user_id)
    if db_todo:
        # Handle case-insensitive priority mapping
        todo_data = todo_update.model_dump(exclude_unset=True)
        for key, value in todo_data.items():
            if key == 'priority' and isinstance(value, str):
                # Map lowercase priority strings to the correct enum values
                if value.lower() == 'high':
                    value = PriorityEnum.high
                elif value.lower() == 'medium':
                    value = PriorityEnum.medium
                elif value.lower() == 'low':
                    value = PriorityEnum.low
            setattr(db_todo, key, value)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
    return db_todo


def delete_todo(session: Session, todo_id: int, user_id: int) -> bool:
    """Delete a specific todo by ID for a specific user.

    Args:
        session: The database session
        todo_id: The ID of the todo to delete
        user_id: The ID of the user who owns this todo

    Returns:
        bool: True if the todo was deleted, False if not found
    """
    db_todo = get_todo_by_id(session, todo_id, user_id)
    if db_todo:
        session.delete(db_todo)
        session.commit()
        return True
    return False


def toggle_todo_completion(session: Session, todo_id: int, user_id: int) -> Optional[Todo]:
    """Toggle the is_completed status of a specific todo for a specific user.

    Args:
        session: The database session
        todo_id: The ID of the todo to toggle completion
        user_id: The ID of the user who owns this todo

    Returns:
        Todo: The updated todo object if successful, None if not found
    """
    db_todo = get_todo_by_id(session, todo_id, user_id)
    if db_todo:
        db_todo.is_completed = not db_todo.is_completed
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
    return db_todo