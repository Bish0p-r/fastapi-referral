from abc import ABC, abstractmethod
from typing import Sequence

from sqlalchemy import RowMapping
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractReadOneRepository(ABC):
    @classmethod
    @abstractmethod
    async def get_one_or_none(cls, session: AsyncSession, **filter_by) -> RowMapping | None:
        ...


class AbstractReadAllRepository(ABC):
    @classmethod
    @abstractmethod
    async def get_all(cls, session: AsyncSession, **filter_by) -> Sequence[RowMapping]:
        ...


class AbstractCreateRepository(ABC):
    @classmethod
    @abstractmethod
    async def create(cls, session: AsyncSession, **data) -> RowMapping:
        ...


class AbstractUpdateRepository(ABC):
    @classmethod
    @abstractmethod
    async def update(cls, session: AsyncSession, data: dict, **filter_by) -> RowMapping | None:
        ...


class AbstractDeleteRepository(ABC):
    @classmethod
    @abstractmethod
    async def delete(cls, session: AsyncSession, **filter_by) -> RowMapping | None:
        ...


class AbstractCRUDRepository(
    AbstractReadOneRepository,
    AbstractReadAllRepository,
    AbstractCreateRepository,
    AbstractUpdateRepository,
    AbstractDeleteRepository,
    ABC,
):
    ...
