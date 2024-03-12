from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    hashed_password: str
    redeemed_token_id: UUID


class EmailSchema(BaseModel):
    email: EmailStr
