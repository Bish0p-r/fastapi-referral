from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession


class AbstractUserServices(ABC):
    @abstractmethod
    async def get_users_by_referrer_id(self, referrer_id: UUID, session: AsyncSession):
        ...
