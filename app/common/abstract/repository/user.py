from abc import ABC

from app.common.abstract.repository.base import AbstractCRUDRepository


class AbstractUserRepository(AbstractCRUDRepository, ABC):
    ...
