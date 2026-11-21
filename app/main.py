from fastapi import FastAPI

from app.api.routes import todos

app = FastAPI(title="FastAPI Study")

app.include_router(todos.router)

@app.get("/health")
def health_check():
  return { "status": "ok"}