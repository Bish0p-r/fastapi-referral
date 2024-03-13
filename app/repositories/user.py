from typing import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.common.abstract.repository.user import AbstractUserRepository
from app.common.base.repository import BaseRepository
from app.models.user import User
from app.models.token import ReferralToken


class UserRepository(BaseRepository, AbstractUserRepository):
    model = User

    @classmethod
    async def get_by_referrer_id(cls, session: AsyncSession, referrer_id: UUID) -> Sequence[User]:
        query = select(
            User
        ).join(
            ReferralToken, User.redeemed_token_id == ReferralToken.id
        ).where(
            ReferralToken.owner_id == referrer_id
        )
        result = await session.execute(query)
        return result.scalars().all()
