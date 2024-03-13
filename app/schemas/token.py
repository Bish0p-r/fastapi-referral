from datetime import datetime, timedelta
from uuid import UUID

from pydantic import BaseModel, Field

from app.schemas.user import UserSchema


class ReferralTokenInSchema(BaseModel):
    token_name: str
    expires_at: datetime = Field(default=datetime.utcnow() + timedelta(days=7))


class ReferralTokenOutSchema(ReferralTokenInSchema):
    id: UUID
    owner_id: UUID


class ReferralTokenNestedOutSchema(ReferralTokenOutSchema):
    owner: UserSchema
