from typing import Annotated

import httpx
from fastapi import APIRouter, BackgroundTasks, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.dependencies.auth import GetAuthServices, GetCurrentUser
from app.dependencies.postgresql import GetSession
from app.schemas.auth import RegisterSchema
from app.schemas.jwt import JWTTokenSchema
from app.schemas.user import UserSchema

router = APIRouter(tags=["Auth"], prefix="/auth")


@router.post("/registration", status_code=201)
async def register(
    user_data: RegisterSchema, auth_service: GetAuthServices, bg_tasks: BackgroundTasks, session: GetSession
) -> UserSchema:
    return await auth_service.registration(user_data.model_dump(mode="json"), bg_tasks, session)


@router.post("/login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], auth_service: GetAuthServices, session: GetSession
) -> JWTTokenSchema:
    access_token = await auth_service.login(form_data.username, form_data.password, session)
    return JWTTokenSchema(access_token=access_token)
