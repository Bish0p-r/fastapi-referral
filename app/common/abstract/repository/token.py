from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from app.common.abstract.repository.base import AbstractCRUDRepository


class AbstractTokenRepository(AbstractCRUDRepository, ABC):
    @classmethod
    @abstractmethod
    async def get_by_owner_email(cls, session: AsyncSession, owner_email: str): ...
