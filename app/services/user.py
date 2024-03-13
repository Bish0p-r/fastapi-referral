from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.common.abstract.repository.user import AbstractUserRepository


class UserServices:
    def __init__(self, user_repository: type[AbstractUserRepository]) -> None:
        self.user_repository = user_repository

    async def get_users_by_referrer_id(self, referrer_id: UUID, session: AsyncSession):
        return await self.user_repository.get_by_referrer_id(session, referrer_id=referrer_id)
