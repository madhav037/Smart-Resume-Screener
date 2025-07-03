from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional
from datetime import datetime
from .enums import UserRole

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    role: UserRole = UserRole.candidate
    profile_picture: Optional[HttpUrl] = None

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
