from abc import ABC

from app.common.abstract.repository.base import AbstractCRUDRepository


class AbstractTokenRepository(AbstractCRUDRepository, ABC):
    ...
