from fastapi import FastAPI, status
from pydantic import BaseModel


class STaskBase(BaseModel):
    name: str
    desc: str | None = None


class STaskAdd(STaskBase):
    pass


class STask(STaskBase):
    id: int


class SUserBase(BaseModel):
    username: str


class SUser(SUserBase):
    pass


class SUserCreate(SUserBase):
    password: str


class SUserRead(SUserBase):
    id: int


class SProduct(BaseModel):
    name: str
    price: int


app = FastAPI()


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_task(task: STaskAdd):
    # task.model_dump().update("id":1)
    task_dict = task.model_dump()
    task_dict["id"] = 1
    return task_dict


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: SUser) -> SUser:
    return user


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    return


@app.post("/start_processing", status_code=status.HTTP_202_ACCEPTED)
async def start_processing():
    return {"message": "Processing started"}


@app.get("/coffee", status_code=status.HTTP_418_IM_A_TEAPOT)
async def get_coffee():
    return


@app.post("/products", status_code=status.HTTP_201_CREATED)
async def create_product(product: SProduct) -> SProduct:
    return product


@app.get("/products", status_code=status.HTTP_200_OK)
async def get_products() -> list:
    return []
