from typing import Annotated

from fastapi import APIRouter, Depends

from app.schemas.auth import LoginSchema, RegisterSchema


router = APIRouter(
    tags=['Auth'],
    prefix='/auth'
)


@router.post('/registration')
async def register(user_data: Annotated[RegisterSchema, Depends()]):
    pass


@router.post('/login')
async def login(user_data: Annotated[LoginSchema, Depends()]):
    pass

