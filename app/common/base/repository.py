from typing import Sequence

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.abstract.repository.base import AbstractCRUDRepository
from app.common.base.model import BaseSqlModel


class BaseRepository(AbstractCRUDRepository):
    model = BaseSqlModel

    @classmethod
    async def get_one_or_none(cls, session: AsyncSession, **filter_by) -> model | None:
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalars().one_or_none()

    @classmethod
    async def get_all(cls, session: AsyncSession, **filter_by) -> Sequence[model]:
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def create(cls, session: AsyncSession, **data) -> model | None:
        query = insert(cls.model).values(**data).returning(cls.model)
        result = await session.execute(query)
        await session.commit()
        return result.scalars().one_or_none()

    @classmethod
    async def delete(cls, session: AsyncSession, **filter_by) -> model | None:
        query = delete(cls.model).filter_by(**filter_by).returning(cls.model)
        result = await session.execute(query)
        await session.commit()
        return result.scalars().one_or_none()

    @classmethod
    async def update(cls, session: AsyncSession, data: dict, **filter_by) -> model | None:
        query = update(cls.model).values(**data).filter_by(**filter_by).returning(cls.model)
        result = await session.execute(query)
        await session.commit()
        return result.scalars().one_or_none()
