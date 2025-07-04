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
    
class UserUpdate(UserBase):
    password: Optional[str] = None
    phone: Optional[str] = None
    profile_picture: Optional[HttpUrl] = None
    name: Optional[str] = None

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
        
class UserPasswordUpdate(BaseModel):
    current_password: str
    new_password: str
