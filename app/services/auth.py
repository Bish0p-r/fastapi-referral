from cashews import cache
from fastapi import BackgroundTasks
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.abstract.repository.user import AbstractUserRepository
from app.common.abstract.services.auth import AbstractAuthService
from app.common.abstract.services.clearbit import AbstractClearbitServices
from app.common.abstract.services.jwt import AbstractJWTServices
from app.common.abstract.services.token import AbstractTokenServices
from app.common.exceptions import InvalidPasswordException, InvalidUsernameException, NonUniqueEmailOrUsernameException
from app.common.utils.auth import get_hash_password, verify_password
from app.models.user import User


class AuthServices(AbstractAuthService):
    def __init__(
        self,
        user_repository: type[AbstractUserRepository],
        jwt_token_services: AbstractJWTServices,
        clearbit_services: AbstractClearbitServices,
        ref_token_services: AbstractTokenServices,
    ) -> None:
        self.user_repository = user_repository
        self.jwt_token_services = jwt_token_services
        self.clearbit_services = clearbit_services
        self.ref_token_services = ref_token_services

    async def login(self, username: str, password: str, session: AsyncSession) -> str:
        existed_user = await self.user_repository.get_one_or_none(session, username=username)
        if existed_user is None:
            raise InvalidUsernameException

        if not verify_password(password, existed_user.hashed_password):
            raise InvalidPasswordException

        access_token = await self.jwt_token_services.create_access_token({"sub": str(existed_user.id)})
        return access_token

    async def registration(self, user_data: dict, bg_tasks: BackgroundTasks, session: AsyncSession) -> User:
        existed_token = None
        token = user_data.get("referral_token")
        if token is not None:
            existed_token = await self.ref_token_services.verify_token(token, session)

        hashed_password = get_hash_password(user_data.get("password"))

        try:
            user = await self.user_repository.create(
                session,
                username=user_data.get("username"),
                email=user_data.get("email"),
                hashed_password=hashed_password,
                redeemed_token_id=existed_token.id if existed_token else None,
            )
        except IntegrityError:
            raise NonUniqueEmailOrUsernameException

        if existed_token is not None:
            await cache.delete(f"users_by_referrer_id:{existed_token.owner_id}")

        bg_tasks.add_task(self.clearbit_services.update_user_data, user.email, session)
        return user
