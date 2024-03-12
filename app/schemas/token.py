from datetime import timedelta

from pydantic import BaseModel, Field, ConfigDict


class ReferralTokenSchema(BaseModel):
    token: str
    ttl: timedelta = Field(default=timedelta(days=7))
    model_config = ConfigDict(ser_json_timedelta="float")
