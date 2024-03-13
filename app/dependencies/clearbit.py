from httpx import AsyncClient

from app.repositories.user import UserRepository
from app.services.clearbit import ClearbitServices


async def get_clearbit_services() -> ClearbitServices:
    return ClearbitServices(client=AsyncClient(), user_repository=UserRepository)
