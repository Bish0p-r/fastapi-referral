from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi.responses import JSONResponse

from app.common.abstract.repository.token import AbstractTokenRepository
from app.common.exceptions import (
    NonUniqueReferralTokenException, ReferralTokenAlreadyExistsException, ReferralTokenDoesNotExistException
)
from app.models.user import User


class TokenServices:
    def __init__(self, token_repository: type[AbstractTokenRepository]) -> None:
        self.token_repository = token_repository

    async def create_token(self, user: User, data: dict, session: AsyncSession):
        existed_token = await self.token_repository.get_one_or_none(session, owner_id=user.id)
        if existed_token is not None:
            raise ReferralTokenAlreadyExistsException
        try:
            token = await self.token_repository.create(session, **data, owner_id=user.id)
        except IntegrityError:
            raise NonUniqueReferralTokenException
        return token

    async def delete_token(self, user: User, session: AsyncSession) -> JSONResponse:
        deleted_token = await self.token_repository.delete(session, owner_id=user.id)
        if deleted_token is None:
            raise ReferralTokenDoesNotExistException
        return JSONResponse(status_code=200, content={"message": "referral token deleted"})

    async def get_token_by_user_email(self, user_email: str, session: AsyncSession):
        return await self.token_repository.get_by_owner_email(session, owner_email=user_email)
