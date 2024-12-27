from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def post_user_info(username: Annotated[str, Path(min_length=5, max_length=20,
                                                      pattern="^[a-zA-Z0-9_-]+$",
                                                      description="Enter username")],
                        age: Annotated[int, Path(ge=18, le=120, title="Age",
                                                 description="Enter age")]):
    user_id = max(int(user) for user in users.keys()) + 1 if users else 1
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: Annotated[int, Path(gt=0, le=100, title="User ID",
                                                description="ID должно быть больше 0 или равно 100")],
                   username: Annotated[str, Path(min_length=5, max_length=20,
                                                 pattern="^[a-zA-Z0-9_-]+$",
                                                 description="Enter username")],
                   age: Annotated[int, Path(ge=18, le=120, title="Age",
                                            description="Enter age")]):
    ids = list(users.keys())
    if ids[user_id-1] != user_id:
        print('Пользователя с таким id нет')
    else:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(gt=0, le=100, title="User ID",
                                                description="ID должно быть больше 0 или равно 100")]):
    del users[user_id]
    return f"The user {user_id} has been deleted"
