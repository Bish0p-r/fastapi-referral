from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import JSON, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.common.base.model import BaseSqlModel

if TYPE_CHECKING:
    from app.models.token import ReferralToken


class User(BaseSqlModel):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(100), nullable=False)

    additional_info: Mapped[JSON] = mapped_column(JSON, nullable=True)

    redeemed_token_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("referralToken.id", ondelete="SET NULL"), nullable=True
    )
    redeemed_token: Mapped["ReferralToken"] = relationship(
        "ReferralToken", back_populates="referrals", foreign_keys=redeemed_token_id
    )

    referral_token: Mapped["ReferralToken"] = relationship(
        "ReferralToken", back_populates="owner", foreign_keys="ReferralToken.owner_id"
    )
