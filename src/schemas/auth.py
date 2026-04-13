from pydantic import BaseModel


class CreateToken(BaseModel):
    access_token: str
    token_type: str
