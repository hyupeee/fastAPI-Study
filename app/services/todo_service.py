from fastapi import HTTPException, status

from app.repositories.todo_repository import todo_repository
from app.schemas.todo import Todo, TodoCreate

def get_todos() -> list[Todo]:
  return todo_repository.find_all()

def get_todo(todo_id: int) -> Todo:
  todo = todo_repository.find_by_id(todo_id)
  if todo is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")
  return todo

def create_todo(data: TodoCreate) -> Todo:
  return todo_repository.save(data)

def update_todo(todo_id: int, data: TodoCreate) -> Todo:
  get_todo(todo_id)
  return todo_repository.update(todo_id, data)

def delete_todo(todo_id: int) -> None:
  get_todo(todo_id)
  todo_repository.delete(todo_id)