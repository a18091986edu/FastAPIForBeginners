from fastapi import APIRouter, Depends
from crud import create_user, get_users



from sqlalchemy import Select

from schemas.user import User, UserAdd
from models.users import UserModel

from database import SessionDep

router = APIRouter(prefix="/users", tags=["Пользователи"])

@router.post("", response_model=User)
async def create_user_router(user: UserAdd, session: SessionDep): 
    return await create_user(user, session)

@router.get("")
async def get_users_router(session: SessionDep): 
    return await get_users(session)