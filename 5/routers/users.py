from fastapi import APIRouter

users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.get("")
async def get_users():
    return ["user1", "user2"]
