from abc import ABC, abstractmethod
from typing import Generic, Sequence, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")


class AbstractReadOneRepository(ABC, Generic[T]):
    @classmethod
    @abstractmethod
    async def get_one_or_none(cls, session: AsyncSession, **filter_by) -> T | None: ...


class AbstractReadAllRepository(ABC, Generic[T]):
    @classmethod
    @abstractmethod
    async def get_all(cls, session: AsyncSession, **filter_by) -> Sequence[T]: ...


class AbstractCreateRepository(ABC, Generic[T]):
    @classmethod
    @abstractmethod
    async def create(cls, session: AsyncSession, **data) -> T: ...


class AbstractUpdateRepository(ABC, Generic[T]):
    @classmethod
    @abstractmethod
    async def update(cls, session: AsyncSession, data: dict, **filter_by) -> T | None: ...


class AbstractDeleteRepository(ABC, Generic[T]):
    @classmethod
    @abstractmethod
    async def delete(cls, session: AsyncSession, **filter_by) -> T | None: ...
