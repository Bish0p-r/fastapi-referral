from uuid import UUID

from cashews import cache
from fastapi import APIRouter

from app.config import settings
from app.dependencies.auth import GetCurrentUser
from app.dependencies.postgresql import GetSession
from app.dependencies.user import GetUserServices
from app.schemas.user import UserAddInfoSchema, UserSchema

router = APIRouter(tags=["Users"], prefix="/users")


@router.get("/me", responses={200: {"model": UserAddInfoSchema}})
async def get_my_profile(user: GetCurrentUser):
    return user


@router.get("/{referrer_user_id}", responses={200: {"model": list[UserSchema]}}, description="Get referred users")
@cache(ttl=settings.CACHE_TTL, key="users_by_referrer_id:{referrer_user_id}")
async def get_users_by_referrer_id(referrer_user_id: UUID, user_services: GetUserServices, session: GetSession):
    return await user_services.get_users_by_referrer_id(referrer_user_id, session)
