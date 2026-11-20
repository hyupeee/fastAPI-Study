from fastapi import FastAPI

app = FastAPI(title="FastAPI Study")

@app.get("/health")
def health_check():
  return { "status": "ok"}