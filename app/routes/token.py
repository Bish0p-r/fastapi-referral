from typing import Annotated
from uuid import uuid4

from fastapi import APIRouter, Depends
from pydantic import EmailStr

from app.schemas.token import ReferralTokenSchema


router = APIRouter(
    tags=['Token'],
    prefix='/token'
)


@router.post('')
async def create_token(token_data: Annotated[ReferralTokenSchema, Depends()]):
    print(token_data.ttl)


@router.get('/{user_email}')
async def get_token_by_email(user_email: EmailStr):
    pass


@router.delete('/{token_id}')
async def delete_token(token_id: uuid4):
    pass

