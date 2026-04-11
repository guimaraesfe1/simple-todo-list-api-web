from fastapi import FastAPI

from src.routes import task, user


app = FastAPI(title="ToDo List API", version="1.0.0")

app.include_router(user.router, prefix="/api/v1")
app.include_router(task.router, prefix="/api/v1")
