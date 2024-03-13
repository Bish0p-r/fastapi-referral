from cashews import cache
from fastapi import FastAPI

from app.config import settings
from app.routes.auth import router as auth_router
from app.routes.token import router as token_router
from app.routes.users import router as users_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(token_router)
app.include_router(users_router)


@app.on_event("startup")
async def startup() -> None:
    cache.setup("redis://0.0.0.0/")
