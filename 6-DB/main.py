from contextlib import asynccontextmanager
from database import engine, Model
from fastapi import FastAPI
from routers.tasks import router as tasks_router
from routers.users import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        #метод create_all - синхронный (блокирующий), а наш движок - асинхронный. этой строкой мы говорим асинхронному движку, чтобы он выполнил синхронную работу в отдельном потоке и вернулся, когда закончит
        await conn.run_sync(Model.metadata.create_all)
    print("DB ready")
    yield
    print("Server shutdown")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
app.include_router(users_router)



@app.get("/")
async def root():
    return {"message": "Hello World"}