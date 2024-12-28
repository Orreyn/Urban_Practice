from typing import Annotated, List
from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def post_user_info(username: Annotated[str, Path(min_length=5, max_length=20,
                                                       pattern="^[a-zA-Z0-9_-]+$",
                                                       description="Enter username")],
                         age: Annotated[int, Path(ge=18, le=120, title="Age",
                                                  description="Enter age")]):
    user_id = max((user.id for user in users), default=0) + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: Annotated[int, Path(gt=0, le=100, title="User ID",
                                                description="ID должно быть больше 0 или равно 100")],
                   username: Annotated[str, Path(min_length=5, max_length=20,
                                                 pattern="^[a-zA-Z0-9_-]+$",
                                                 description="Enter username")],
                   age: Annotated[int, Path(ge=18, le=120, title="Age",
                                            description="Enter age")]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(gt=0, le=100, title="User ID",
                                                   description="ID должно быть больше 0 или равно 100")]):
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return user
    raise HTTPException(status_code=404, detail="User was not found")
