from typing import Annotated, List
from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from starlette.templating import _TemplateResponse

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []
users.append(User(id=1, username='Feather', age=20))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_users(user_id: int, request: Request):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")


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
