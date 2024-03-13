from app.common.abstract.repository.token import AbstractTokenRepository
from app.common.base.repository import BaseRepository
from app.models.token import ReferralToken


class TokenRepository(BaseRepository, AbstractTokenRepository):
    model = ReferralToken
