from pydantic import BaseModel, EmailStr, Field, model_validator


class RegisterSchema(BaseModel):
    email: EmailStr = Field(max_length=100)
    username: str = Field(max_length=50)
    referral_token: str | None = None
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def check_passwords_match(self):
        pw1 = self.password
        pw2 = self.confirm_password

        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError("passwords do not match")
        return self


class LoginSchema(BaseModel):
    username: str = Field(max_length=50)
    password: str
