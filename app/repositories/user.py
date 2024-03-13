from app.common.abstract.repository.user import AbstractUserRepository
from app.common.base.repository import BaseRepository
from app.models.user import User


class UserRepository(BaseRepository, AbstractUserRepository):
    model = User
