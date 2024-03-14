from abc import ABC, abstractmethod
from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from app.common.base.model import BaseSqlModel


class AbstractReadOneRepository(ABC):
    model = BaseSqlModel

    @classmethod
    @abstractmethod
    async def get_one_or_none(cls, session: AsyncSession, **filter_by) -> model | None: ...


class AbstractReadAllRepository(ABC):
    model = BaseSqlModel

    @classmethod
    @abstractmethod
    async def get_all(cls, session: AsyncSession, **filter_by) -> Sequence[model]: ...


class AbstractCreateRepository(ABC):
    model = BaseSqlModel

    @classmethod
    @abstractmethod
    async def create(cls, session: AsyncSession, **data) -> model: ...


class AbstractUpdateRepository(ABC):
    model = BaseSqlModel

    @classmethod
    @abstractmethod
    async def update(cls, session: AsyncSession, data: dict, **filter_by) -> model | None: ...


class AbstractDeleteRepository(ABC):
    model = BaseSqlModel

    @classmethod
    @abstractmethod
    async def delete(cls, session: AsyncSession, **filter_by) -> model | None: ...


class AbstractCRUDRepository(
    AbstractReadOneRepository,
    AbstractReadAllRepository,
    AbstractCreateRepository,
    AbstractUpdateRepository,
    AbstractDeleteRepository,
    ABC,
): ...
