from pydantic import BaseModel, EmailStr
from typing import Optional


class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    country: str
    whatsapp: str
    telegram: Optional[str] = ""
    level: Optional[str] = ""
    goal: Optional[str] = ""


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    country: str
    whatsapp: str
    telegram: str
    level: str
    goal: str
    role: str

    class Config:
        from_attributes = True