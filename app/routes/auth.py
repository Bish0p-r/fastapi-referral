from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.auth import RegisterSchema
from app.schemas.jwt import JWTTokenSchema
from app.dependencies.auth import GetAuthServices, GetCurrentUser
from app.dependencies.postgresql import GetSession
from app.schemas.user import UserSchema

router = APIRouter(
    tags=['Auth'],
    prefix='/auth'
)


@router.post('/registration', status_code=201)
async def register(
        user_data: Annotated[RegisterSchema, Depends()],
        auth_service: GetAuthServices,
        session: GetSession
) -> UserSchema:
    return await auth_service.registration(user_data.model_dump(mode="json"), session)


@router.post('/login')
async def login(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        auth_service: GetAuthServices,
        session: GetSession
) -> JWTTokenSchema:
    access_token = await auth_service.login(form_data.username, form_data.password, session)
    return JWTTokenSchema(access_token=access_token)
