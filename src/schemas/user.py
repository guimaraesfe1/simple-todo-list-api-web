from pydantic import BaseModel, EmailStr


class BaseUserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str


class SignUpUserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
