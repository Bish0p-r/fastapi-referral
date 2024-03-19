from typing import Generic, Sequence, TypeVar

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.abstract.repository.base import (
    AbstractCreateRepository,
    AbstractDeleteRepository,
    AbstractReadAllRepository,
    AbstractReadOneRepository,
    AbstractUpdateRepository,
)

T = TypeVar("T")


class BaseRepository(
    Generic[T],
    AbstractReadOneRepository[T],
    AbstractReadAllRepository[T],
    AbstractCreateRepository[T],
    AbstractUpdateRepository[T],
    AbstractDeleteRepository[T]
):
    model: T

    @classmethod
    async def get_one_or_none(cls, session: AsyncSession, **filter_by) -> T | None:
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalars().one_or_none()

    @classmethod
    async def get_all(cls, session: AsyncSession, **filter_by) -> Sequence[T]:
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def create(cls, session: AsyncSession, **data) -> T:
        query = insert(cls.model).values(**data).returning(cls.model)
        result = await session.execute(query)
        await session.commit()
        return result.scalars().one_or_none()

    @classmethod
    async def delete(cls, session: AsyncSession, **filter_by) -> T | None:
        query = delete(cls.model).filter_by(**filter_by).returning(cls.model)
        result = await session.execute(query)
        await session.commit()
        return result.scalars().one_or_none()

    @classmethod
    async def update(cls, session: AsyncSession, data: dict, **filter_by) -> T | None:
        query = update(cls.model).values(**data).filter_by(**filter_by).returning(cls.model)
        result = await session.execute(query)
        await session.commit()
        return result.scalars().one_or_none()
