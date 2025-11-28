from pydantic import SecretStr

from ksecrets.helpers.pydantic import BaseModel


class Password(BaseModel):
    title: str
    url: str
    username: str
    password: SecretStr
    notes: str
    otp_auth: str
