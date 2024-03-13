from pydantic import BaseModel


class JWTTokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
