from typing import Annotated

from fastapi import Depends

from app.repositories.user import UserRepository
from app.services.jwt import JWTServices


async def get_jwt_services() -> JWTServices:
    return JWTServices(user_repository=UserRepository)

GetJWTServices = Annotated[JWTServices, Depends(get_jwt_services)]
