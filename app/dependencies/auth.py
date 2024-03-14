from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.common.exceptions import InvalidTokenException
from app.dependencies.clearbit import get_clearbit_services
from app.dependencies.jwt import GetJWTServices, get_jwt_services
from app.dependencies.postgresql import GetSession
from app.dependencies.token import get_token_services
from app.models.user import User
from app.repositories.user import UserRepository
from app.services.auth import AuthServices


async def get_auth_service() -> AuthServices:
    return AuthServices(
        user_repository=UserRepository,
        jwt_token_services=await get_jwt_services(),
        clearbit_services=await get_clearbit_services(),
        ref_token_services=await get_token_services(),
    )


GetAuthServices = Annotated[AuthServices, Depends(get_auth_service)]


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)], jwt_services: GetJWTServices, session: GetSession
) -> User:
    user = await jwt_services.get_user_from_token(token, session)
    if user is None:
        raise InvalidTokenException
    return user


GetCurrentUser = Annotated[User, Depends(get_current_user)]
