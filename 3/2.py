from pydantic import BaseModel
from fastapi import FastAPI

db = []
tasks = []

items_db = [
    {"name": "Phone", "price": 100, "cost": 50},
    {"name": "Case", "price": 10, "cost": 1},
]


class SItem(BaseModel):
    name: str
    price: int

class SOrder(BaseModel):
    item_name: str
    price: int
    quantity: int

class SUserBase(BaseModel):
    username: str

class SUserCreate(SUserBase):
    password: str

class SUserRead(SUserBase):
    id: int


class SUser(SUserBase):
    pass

class SNote(BaseModel):
    text: str

class STaskBase(BaseModel):
    name: str
    desc: str | None = None

class STaskAdd(STaskBase):
    pass

class STask(STaskBase):
    id: int

class SProductBase(BaseModel):
    title: str
    price: int

class SProductCreate(SProductBase):
    pass

class SProductResponse(SProductBase):
    id: int

class SItemPublic(BaseModel):
    name: str
    price: int

app = FastAPI()

@app.post("/create_item")
async def create_item(item: SItem):
    return item

@app.post("/calc")
async def calc(order: SOrder):
    return {"total_price": order.price * order.quantity}

@app.post("/register")
async def register(user: SUser):
    return user.model_dump(exclude="password")

@app.post("/add_note")
async def add_note(note: SNote):
    db.append(note.model_dump())
    return {"msg": "Note added"}

@app.post("/tasks")
async def tasksfunc(task: STaskAdd):
    full_task = task.model_dump()
    full_task["id"] = len(tasks)+1
    tasks.append(full_task)
    return full_task

@app.get("/user", response_model=SUser)
async def get_user():
    return {
        "username": "johndoe",
        "email": "john@example.com",
        "password": "secret_password_123",
    }

@app.post("/users")
async def create_user(user: SUserCreate) -> SUserRead:
    return SUserRead(id=1, username=user.username)


# @app.get("/items", response_model=list[SItemPublic])
@app.get("/items")
async def get_items() -> list[SItemPublic]:
    return items_db
