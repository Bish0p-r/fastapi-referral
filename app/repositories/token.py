from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.common.abstract.repository.token import AbstractTokenRepository
from app.common.base.repository import BaseRepository
from app.models.token import ReferralToken
from app.models.user import User


class TokenRepository(BaseRepository, AbstractTokenRepository):
    model = ReferralToken

    @classmethod
    async def get_by_owner_email(cls, session: AsyncSession, owner_email: str) -> model | None:
        query = (
            select(cls.model)
            .join(cls.model.owner)
            .options(selectinload(cls.model.owner))
            .where(User.email == owner_email)
        )
        result = await session.execute(query)
        await session.commit()
        return result.scalars().one_or_none()
