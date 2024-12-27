from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
async def read_root() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def get_admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def get_user(user_id: Annotated[int, Path(gt=0, le=100, title="User ID",
                                                description="ID должно быть больше 0 или равно 100")]):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20,
                                                      pattern="^[a-zA-Z0-9_-]+$",
                                                      description="Enter username")],
                        age: Annotated[int, Path(ge=18, le=120, title="Age",
                                                 description="Enter age")]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
