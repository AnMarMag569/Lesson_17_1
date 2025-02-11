from fastapi import FastAPI
from app.routers import user
from app.routers import task

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.user_router)
app.include_router(task.task_router)