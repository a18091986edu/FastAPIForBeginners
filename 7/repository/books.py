from typing import List
from sqlalchemy import select, update, delete, func, and_
from sqlalchemy.ext.asyncio import AsyncSession
from models.books import BooksModel
from schemas.books import SBookAdd


class BooksRepository:

    @classmethod
    async def add_one(cls, data: SBookAdd, session: AsyncSession) -> BooksModel:
        book = BooksModel(**data.model_dump())
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book

    @classmethod
    async def get_all(cls, session: AsyncSession) -> List[BooksModel]:
        query = select(BooksModel)
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def get_one(cls, book_id: int, session: AsyncSession) -> BooksModel:
        query = select(BooksModel).where(BooksModel.id == book_id)
        result = await session.execute(query)
        return result.scalar_one()

    @classmethod
    async def update_one(
        cls, book_id: int, data: SBookAdd, session: AsyncSession
    ) -> BooksModel:
        query = (
            update(BooksModel)
            .where(BooksModel.id == book_id)
            .values(**data.model_dump())
            .returning(BooksModel)
        )
        result = await session.execute(query)
        await session.commit()
        return result.scalar_one()

    @classmethod
    async def delete_one(cls, book_id: int, session: AsyncSession) -> None:
        query = delete(BooksModel).where(BooksModel.id == book_id)
        await session.execute(query)
        await session.commit()
        return None

    @classmethod
    async def search_books(
        cls,
        session: AsyncSession,
        author: str | None = None,
        title: str | None = None,
        year: int | None = None,
    ) -> List[BooksModel]:
        query = select(BooksModel)
        conditions = []
        if author:
            conditions.append(func.lower(BooksModel.author).contains(author.lower()))
        if title:
            conditions.append(func.lower(BooksModel.title).contains(title.lower()))
        if year is not None:
            conditions.append(BooksModel.year == year)
        if conditions:
            query = query.where(and_(*conditions))
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def find_by_is_read(
        cls, is_read: bool, session: AsyncSession
    ) -> List[BooksModel]:
        query = select(BooksModel).where(BooksModel.is_read == is_read)
        result = await session.execute(query)
        books_models = result.scalars().all()
        return books_models
