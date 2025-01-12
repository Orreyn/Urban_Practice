from fastapi import FastAPI
from app.models import user, task

app = FastAPI()


@app.get("/")
async def read_root():
    return {'message': 'Welcome to Taskmanager'}

app.include_router(task.router)
app.include_router(user.router)
