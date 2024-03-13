from datetime import datetime, timedelta

from jose import ExpiredSignatureError, JWTError, jwt

from app.common.abstract.repository.user import AbstractUserRepository
from app.common.abstract.services.jwt import AbstractJWTServices
from app.common.exceptions import ExpiredTokenException, InvalidTokenException
from app.config import settings


class JWTServices(AbstractJWTServices):
    def __init__(self, user_repository: type[AbstractUserRepository]) -> None:
        self.user_repository = user_repository

    @staticmethod
    async def create_token(data: dict, expire_in: timedelta) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + expire_in
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    @staticmethod
    async def decode_token(token: str) -> dict:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        except ExpiredSignatureError:
            raise ExpiredTokenException
        except JWTError:
            raise InvalidTokenException
        return payload

    async def create_access_token(
        self,
        data: dict,
        expire_in: timedelta = timedelta(minutes=settings.ACCESS_TOKEN_EXP_MINUTES),
    ):
        data = data.copy()
        data.update({"type": "access-token"})
        return await self.create_token(data, expire_in=expire_in)

    async def get_user_from_token(self, token: str, session):
        payload = await self.decode_token(token)
        sub = payload.get("sub")

        if sub is None:
            raise InvalidTokenException
        if payload.get("type") != "access-token":
            raise InvalidTokenException

        return await self.user_repository.get_one_or_none(session, id=sub)
