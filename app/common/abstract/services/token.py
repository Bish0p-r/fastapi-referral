from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi.responses import JSONResponse

from app.models.user import User


class AbstractTokenServices(ABC):
    @abstractmethod
    async def create_token(self, user: User, data: dict, session: AsyncSession):
        ...

    @abstractmethod
    async def delete_token(self, user: User, session: AsyncSession) -> JSONResponse:
        ...

    @abstractmethod
    async def get_token_by_user_email(self, user_email: str, session: AsyncSession):
        ...
