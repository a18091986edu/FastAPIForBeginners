from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

users_db = {
    1: {"name": "Alice", "email": "alice@example.com"}
}

tasks_db = {
    1: {"title": "Learn FastAPI", "priority": 1}
}

names = ["Alice", "Bob", "Charlie"]

users_db = {1: {"id": 1, "name": "John", "is_active": True}}

items = ["apple", "banana", "orange"]


class SUserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None

class STaskPatch(BaseModel):
    title: str | None = None
    priority: int | None = None


app = FastAPI()

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: SUserUpdate) -> SUserUpdate:
    if user_id not in users_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    users_db[user_id] = user.model_dump()
    return users_db[user_id]

@app.patch("/tasks/{task_id}")
async def update_task(task_id: int, task: STaskPatch) -> STaskPatch:
    if task_id not in tasks_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    tasks_db[task_id].update(task.model_dump(exclude_unset=True))
    return tasks_db[task_id]

@app.delete("/names/{index}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_name(index: int):
    if index >= len(names):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Index out of range")
    del names[index]
    return

@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    users_db[user_id]["is_active"] = False
    return users_db[user_id]
    
@app.delete("/items/{value}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(value: str):
    if value not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    items.remove(value)
    return
