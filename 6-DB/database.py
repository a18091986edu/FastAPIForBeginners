from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from config import DATABASE_URL

# # DATABASE_URL = "sqlite+aiosqlite:///tasks.db"
engine = create_async_engine(DATABASE_URL, echo=False)

new_session = async_sessionmaker(engine, expire_on_commit=False)
# expire_on_commit = False - критически важно для асинхронности - после коммита (закрытия сессии) данные остаются в памяти и их можно прочитать


class Model(DeclarativeBase, MappedAsDataclass):
    pass


# базовый класс работает как каталог - когда мы создадим новый класс (таблицу), базовый класс автоматически запишет её в свой список
# MappedAsDataclass - миксин, который делает модели похоими на датаклассы - не нужно будет писать __init__ - библиотека сама сгенерирует конструктор на основе полей класса


async def get_db():
    async with new_session() as session:
        yield session


# аннотация говорит: это переменная типа AsyncSession и чтобы её получить требуется выполнить функцию get_db
SessionDep = Annotated[AsyncSession, Depends(get_db)]
