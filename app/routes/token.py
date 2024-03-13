from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import EmailStr

from app.schemas.token import ReferralTokenInSchema, ReferralTokenOutSchema, ReferralTokenNestedOutSchema
from app.dependencies.auth import GetCurrentUser
from app.dependencies.postgresql import GetSession
from app.dependencies.token import GetTokenServices
from app.common.base.schemas import JsonResponseSchema


router = APIRouter(
    tags=['Token'],
    prefix='/token'
)


@router.post('/', status_code=201, responses={201: {"model": ReferralTokenOutSchema}})
async def create_token(
        user: GetCurrentUser,
        token_data: Annotated[ReferralTokenInSchema, Depends()],
        token_services: GetTokenServices,
        session: GetSession
):
    return await token_services.create_token(user, token_data.model_dump(mode="dict"), session)


@router.get('/{user_email}', responses={200: {"model": ReferralTokenNestedOutSchema}})
async def get_token_by_email(
        user_email: EmailStr,
        token_services: GetTokenServices,
        session: GetSession
):
    return await token_services.get_token_by_user_email(user_email, session)


@router.delete('/', responses={200: {"model": JsonResponseSchema}})
async def delete_token(
        user: GetCurrentUser,
        token_services: GetTokenServices,
        session: GetSession
):
    return await token_services.delete_token(user, session)

