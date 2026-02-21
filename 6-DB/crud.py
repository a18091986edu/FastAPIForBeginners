from sqlalchemy import select, delete, insert, update
from models.users import UserModel
from schemas.user import UserAdd
from database import SessionDep

# Select
# query = select(TasksModel)
# query = select(TasksModel).where(TasksModel.id == 2)
# result = await session.execute(query)
# tasks = result.scalars().all()

# #INSERT
# new_task = TasksModel(name="Выучить SQL", description="срочно")
# session.add(new_task)
# await session.commit()

# #DELETE
# stmt = delete(TasksModel).where(TasksModel.id == 2)
# await session.execute(stmt)
# await session.commit()

# Паттерн

# async def create_something(session: SessionDep):
#     obj = MyModel(field="value") #создали объект, id ещё нет
#     session.add(obj) # добавляем в сессию - мы хотим это сохранить, но это ещё не уходит в БД
#     await session.commit() #БД сохраняет строку и присваивает ей id
#     await session.refresh(obj) # делаем запрос к БД, чтобы узнать новый id

#     return obj


async def create_user(user: UserAdd, session: SessionDep):
    new_user = UserModel(**user.model_dump())  # распаковка словаря
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


async def get_users(session: SessionDep):
    query = select(UserModel)
    result = await session.execute(query)
    users = result.scalars().all()
    return users
