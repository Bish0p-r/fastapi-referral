from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    redeemed_token_id: UUID | None


class UserAddInfoSchema(UserSchema):
    additional_info: dict | None
