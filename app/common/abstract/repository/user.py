from abc import ABC, abstractmethod
from typing import Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.common.abstract.repository.base import AbstractCRUDRepository
from app.models.user import User


class AbstractUserRepository(AbstractCRUDRepository, ABC):

    @classmethod
    @abstractmethod
    async def get_by_referrer_id(cls, session: AsyncSession, referrer_id: UUID) -> Sequence[User]:
        ...
