from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.models.token import ReferralToken


class AbstractTokenServices(ABC):
    @abstractmethod
    async def create_token(self, user: User, data: dict, session: AsyncSession) -> ReferralToken: ...

    @abstractmethod
    async def delete_token(self, user: User, session: AsyncSession) -> JSONResponse: ...

    @abstractmethod
    async def get_token_by_user_email(self, user_email: str, session: AsyncSession) -> ReferralToken: ...

    @abstractmethod
    async def verify_token(self, token_name: str, session: AsyncSession) -> ReferralToken: ...
