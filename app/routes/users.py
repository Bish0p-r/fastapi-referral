from uuid import UUID

from fastapi import APIRouter


router = APIRouter(
    tags=['Users'],
    prefix='/users'
)


@router.get('/{referrer_user_id}')
async def get_users(referrer_user_id: UUID):
    return

