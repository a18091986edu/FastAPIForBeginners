from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine, Base
from routers.books import router as books_router




@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("БД готова к работе")
    yield
    print("Выключение сервера")


app = FastAPI(lifespan=lifespan)
app.include_router(books_router)
