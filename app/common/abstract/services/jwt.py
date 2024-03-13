from abc import ABC, abstractmethod
from datetime import timedelta

from app.config import settings


class AbstractJWTServices(ABC):

    @staticmethod
    @abstractmethod
    async def create_token(data: dict, expire_in: timedelta) -> str: ...

    @staticmethod
    @abstractmethod
    async def decode_token(token: str) -> dict: ...

    @abstractmethod
    async def create_access_token(
        self,
        data: dict,
        expire_in: timedelta = timedelta(minutes=settings.ACCESS_TOKEN_EXP_MINUTES),
    ): ...

    @abstractmethod
    async def get_user_from_token(self, token: str, session): ...
