from app.schemas.todo import TodoCreate, Todo

class TodoRepository:
  """ TODO : DB 교체 예정 """
  
  def __init__(self) -> None:
    self._store: dict[int, Todo] = {}
    self._next_id = 1
    
  def find_all(self) -> list[Todo]:
    return list(self._store.values())
  
  def find_by_id(self, todo_id: int) -> Todo | None:
    return self._store.get(todo_id)
  
  def save(self, data: TodoCreate) -> Todo:
    todo = Todo(id=self._next_id, **data.model_dump())
    self._store[todo.id] = todo
    self._next_id += 1
    return todo
  
  def update(self, todo_id: int, data: TodoCreate) -> Todo:
    todo = Todo(id=todo_id, **data.model_dump())
    self._store[todo_id] = todo
    return todo
  
  def delete(self, todo_id: int) -> None:
    self._store.pop(todo_id, None)
    
todo_repository = TodoRepository()