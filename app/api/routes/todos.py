from fastapi import APIRouter, status

from app.schemas.todo import Todo, TodoCreate
from app.services import todo_service

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("", response_model=list[Todo])
def list_todos():
  return todo_service.get_todos()

@router.get("/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
  return todo_service.get_todo(todo_id)

@router.post("", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(body: TodoCreate):
  return todo_service.create_todo(body)

@router.put("/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, body: TodoCreate):
  return todo_service.update_todo(todo_id, body)

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
  todo_service.delete_todo(todo_id)