from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class AbstractClearbitServices(ABC):
    @abstractmethod
    async def get_user_data(self, email: str) -> dict | None: ...

    @abstractmethod
    async def update_user_data(self, email: str, session: AsyncSession) -> None: ...
