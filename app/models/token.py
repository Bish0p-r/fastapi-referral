from datetime import datetime, timedelta
from typing import TYPE_CHECKING, List
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.common.base.model import BaseSqlModel

if TYPE_CHECKING:
    from app.models.user import User


class ReferralToken(BaseSqlModel):
    __tablename__ = "referralToken"

    token_name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    owner_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("user.id"), nullable=False, unique=True)
    owner: Mapped["User"] = relationship("User", back_populates="referral_token", foreign_keys=[owner_id])

    referrals: Mapped[List["User"]] = relationship(
        "User", back_populates="redeemed_token", foreign_keys="User.redeemed_token_id"
    )
