from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class AbstractAuthService(ABC):
    @abstractmethod
    async def login(self, username: str, password: str, session: AsyncSession):
        ...

    @abstractmethod
    async def registration(self, user_data: dict, session: AsyncSession):
        ...
