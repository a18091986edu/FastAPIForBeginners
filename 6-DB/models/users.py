from sqlalchemy.orm import Mapped, mapped_column
from database import Model


class UserModel(Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str]
