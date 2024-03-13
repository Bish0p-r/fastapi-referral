from typing import Annotated

from fastapi import Depends

from app.services.token import TokenServices
from app.repositories.token import TokenRepository


async def get_token_services():
    return TokenServices(token_repository=TokenRepository)

GetTokenServices = Annotated[TokenServices, Depends(get_token_services)]
