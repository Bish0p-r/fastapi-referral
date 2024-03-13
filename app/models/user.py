from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.common.base.model import BaseSqlModel


if TYPE_CHECKING:
    from app.models.token import ReferralToken


class User(BaseSqlModel):
    __tablename__ = 'user'

    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(100), nullable=False)

    redeemed_token_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('referralToken.id'), nullable=True)

    referral_token: Mapped["ReferralToken"] = relationship('ReferralToken', back_populates='owner')
