from uuid import UUID

from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.abstract.repository.user import AbstractUserRepository
from app.common.abstract.services.user import AbstractUserServices
from app.models.user import User


class UserServices(AbstractUserServices):
    def __init__(self, user_repository: type[AbstractUserRepository]) -> None:
        self.user_repository = user_repository

    async def get_users_by_referrer_id(self, referrer_id: UUID, session: AsyncSession) -> Sequence[User]:
        return await self.user_repository.get_by_referrer_id(session, referrer_id=referrer_id)
