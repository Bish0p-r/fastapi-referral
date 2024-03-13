from typing import Annotated

from cashews import cache
from fastapi import APIRouter, Depends
from pydantic import EmailStr

from app.config import settings
from app.schemas.token import ReferralTokenInSchema, ReferralTokenOutSchema, ReferralTokenNestedOutSchema
from app.dependencies.auth import GetCurrentUser
from app.dependencies.postgresql import GetSession
from app.dependencies.token import GetTokenServices
from app.common.base.schemas import JsonResponseSchema


router = APIRouter(
    tags=['Token'],
    prefix='/token'
)


@router.get('/', responses={200: {"model": ReferralTokenNestedOutSchema}})
@cache(ttl=settings.CACHE_TTL, key='token_by_user_email:{user.email}')
async def get_my_token(
        user: GetCurrentUser,
        token_services: GetTokenServices,
        session: GetSession
):
    return await token_services.get_token_by_user_email(user.email, session)


@router.get('/{user_email}', responses={200: {"model": ReferralTokenNestedOutSchema}})
@cache(ttl=settings.CACHE_TTL, key='token_by_user_email:{user_email}')
async def get_token_by_email(
        user_email: EmailStr,
        token_services: GetTokenServices,
        session: GetSession
):
    return await token_services.get_token_by_user_email(user_email, session)


@router.post('/', status_code=201, responses={201: {"model": ReferralTokenOutSchema}})
@cache.invalidate(key_template="token_by_user_email:{user.email}")
@cache.invalidate(key_template="users_by_referrer_id:{user.id}")
async def create_token(
        user: GetCurrentUser,
        token_data: Annotated[ReferralTokenInSchema, Depends()],
        token_services: GetTokenServices,
        session: GetSession
):
    return await token_services.create_token(user, token_data.model_dump(mode="dict"), session)


@router.delete('/', responses={200: {"model": JsonResponseSchema}})
@cache.invalidate(key_template="token_by_user_email:{user.email}")
async def delete_token(
        user: GetCurrentUser,
        token_services: GetTokenServices,
        session: GetSession
):
    return await token_services.delete_token(user, session)
