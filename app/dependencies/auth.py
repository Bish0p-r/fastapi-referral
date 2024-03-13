from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.services.auth import AuthServices
from app.repositories.user import UserRepository
from app.repositories.token import TokenRepository
from app.dependencies.jwt import get_jwt_services, GetJWTServices
from app.dependencies.postgresql import GetSession
from app.models.user import User
from app.common.exceptions import InvalidTokenException


async def get_auth_service():
    return AuthServices(
        user_repository=UserRepository,
        ref_token_repository=TokenRepository,
        jwt_token_services=await get_jwt_services()
    )


GetAuthServices = Annotated[AuthServices, Depends(get_auth_service)]


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        jwt_services: GetJWTServices,
        session: GetSession
) -> User:
    user = await jwt_services.get_user_from_token(token, session)
    if user is None:
        raise InvalidTokenException
    return user

GetCurrentUser = Annotated[User, Depends(get_current_user)]
