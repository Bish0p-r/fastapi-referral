from httpx import AsyncClient

from app.services.clearbit import ClearbitServices
from app.repositories.user import UserRepository


async def get_clearbit_services() -> ClearbitServices:
    return ClearbitServices(client=AsyncClient(), user_repository=UserRepository)


