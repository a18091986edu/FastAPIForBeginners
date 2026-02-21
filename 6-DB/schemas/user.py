from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    name: str


class UserAdd(UserBase):
    pass


class User(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
