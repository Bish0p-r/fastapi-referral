from fastapi import FastAPI

from app.routes.auth import router as auth_router
from app.routes.token import router as token_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(token_router)


