from uuid import UUID

from cashews import cache
from fastapi import APIRouter

from app.config import settings
from app.dependencies.postgresql import GetSession
from app.dependencies.user import GetUserServices
from app.schemas.user import UserSchema


router = APIRouter(
    tags=['Users'],
    prefix='/users'
)


@router.get('/{referrer_user_id}', responses={200: {"model": list[UserSchema]}})
@cache(ttl=settings.CACHE_TTL, key='users_by_referrer_id:{referrer_user_id}')
async def get_users_by_referrer_id(
        referrer_user_id: UUID,
        user_services: GetUserServices,
        session: GetSession
) -> list[UserSchema]:
    return await user_services.get_users_by_referrer_id(referrer_user_id, session)

