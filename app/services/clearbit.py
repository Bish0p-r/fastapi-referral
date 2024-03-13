from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.abstract.repository.user import AbstractUserRepository
from app.common.abstract.services.clearbit import AbstractClearbitServices
from app.config import settings


class ClearbitServices(AbstractClearbitServices):
    def __init__(self, client: AsyncClient, user_repository: type[AbstractUserRepository]) -> None:
        self.client = client
        self.user_repository = user_repository

    async def get_user_data(self, email: str) -> dict | None:
        response = await self.client.get(
            f"https://person.clearbit.com/v1/people/email/{email}",
            headers={"Authorization": f"Bearer {settings.CLEARBIT_API_KEY}"},
        )
        if response.status_code == 200:
            return response.json()

    async def update_user_data(self, email: str, session: AsyncSession) -> None:
        data = await self.get_user_data(email)
        if data is not None:
            await self.user_repository.update(session, {"additional_info": data}, email=email)
