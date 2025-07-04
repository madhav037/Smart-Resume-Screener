from pydantic import BaseModel, EmailStr
from .enums import UserRole

class UserCreate(BaseModel):
    name : str
    email : EmailStr
    password : str
    role : UserRole
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str 