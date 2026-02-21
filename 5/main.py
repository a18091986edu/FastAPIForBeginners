from fastapi import FastAPI, APIRouter

# from routers.ping import router as ping_router
from routers.users import users_router

app = FastAPI()
# app.include_router(ping_router)
# app.include_router(users_router)
