from datetime import datetime, timedelta
from uuid import uuid4
from typing import TYPE_CHECKING

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.common.base.model import BaseSqlModel


if TYPE_CHECKING:
    from app.models.user import User


class ReferralToken(BaseSqlModel):
    __tablename__ = 'referralToken'

    token: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    ttl: Mapped[timedelta] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow + ttl)

    owner_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('user.id'), nullable=False)
    owner: Mapped["User"] = relationship('User', back_populates='referral_token')

