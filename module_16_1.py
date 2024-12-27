from typing import Set

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    age: int


@app.get("/")
async def read_root() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def get_admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def get_user(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def get_user_info(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
