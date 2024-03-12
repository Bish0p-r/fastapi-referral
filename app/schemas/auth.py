from pydantic import BaseModel, model_validator


class RegisterSchema(BaseModel):
    email: str
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
    email: str
    password: str