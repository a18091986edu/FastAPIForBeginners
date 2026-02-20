from pydantic import BaseModel, Field
from fastapi import FastAPI

app = FastAPI()

class SUser(BaseModel):
    name: str
    age: int
    is_active: bool = True

class SProduct(BaseModel):
    title: str
    price: int
    description: str | None = None

class SFeedBack(BaseModel):
    message: str
    rating: int = Field(..., ge=1, le=5)


class SRegistration(BaseModel):
    username: str = Field(..., min_length=5, max_length=20)
    bio: str = Field("", max_length=100)

class STaskAdd(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Название задачи")
    description: str | None = Field(None, max_length=300)
    priority: int = Field(1, ge=1, le=5, description="Приоритет задачи")

@app.post("/tasks")
async def add_task(task: STaskAdd):
    return {"message": "Задача получена",
            "data": task}


