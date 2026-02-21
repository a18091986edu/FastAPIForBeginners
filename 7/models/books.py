from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class BooksModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    year: Mapped[int | None]
    pages: Mapped[int | None]
    is_read: Mapped[bool] = mapped_column(default=False)
