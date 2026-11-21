from pydantic import BaseModel, Field

class TodoCreate(BaseModel):
  """ 생성/수정 요청 DTO """
  title: str = Field(min_length=1, max_length=100)
  done: bool = False
  
class Todo(TodoCreate):
  """ 응답 DTO = TodoCreate 필드 + id """
  id: int