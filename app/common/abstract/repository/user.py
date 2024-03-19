from abc import ABC, abstractmethod
from typing import Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.common.abstract.repository.base import (
    AbstractCreateRepository,
    AbstractDeleteRepository,
    AbstractReadAllRepository,
    AbstractReadOneRepository,
    AbstractUpdateRepository,
)
from app.models.user import User


class AbstractUserRepository(
    AbstractReadOneRepository[User],
    AbstractReadAllRepository[User],
    AbstractCreateRepository[User],
    AbstractUpdateRepository[User],
    AbstractDeleteRepository[User],
    ABC
):
    @classmethod
    @abstractmethod
    async def get_by_referrer_id(cls, session: AsyncSession, referrer_id: UUID) -> Sequence[User]: ...
