from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from app.common.abstract.repository.base import (
    AbstractCreateRepository,
    AbstractDeleteRepository,
    AbstractReadAllRepository,
    AbstractReadOneRepository,
    AbstractUpdateRepository,
)
from app.models.token import ReferralToken


class AbstractTokenRepository(
    AbstractReadOneRepository[ReferralToken],
    AbstractReadAllRepository[ReferralToken],
    AbstractCreateRepository[ReferralToken],
    AbstractUpdateRepository[ReferralToken],
    AbstractDeleteRepository[ReferralToken],
    ABC
):

    @classmethod
    @abstractmethod
    async def get_by_owner_email(cls, session: AsyncSession, owner_email: str) -> ReferralToken | None: ...
