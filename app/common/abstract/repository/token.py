from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from app.common.abstract.repository.base import AbstractCRUDRepository
from app.models.token import ReferralToken


class AbstractTokenRepository(AbstractCRUDRepository, ABC):
    model = ReferralToken

    @classmethod
    @abstractmethod
    async def get_by_owner_email(cls, session: AsyncSession, owner_email: str) -> model: ...
