from typing import Annotated

from fastapi import Depends

from app.repositories.token import TokenRepository
from app.services.token import TokenServices


async def get_token_services():
    return TokenServices(token_repository=TokenRepository)


GetTokenServices = Annotated[TokenServices, Depends(get_token_services)]
