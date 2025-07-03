from pydantic import BaseModel, EmailStr, HttpUrl
from datetime import datetime

class ResumeBase(BaseModel):
    name: str
    email: EmailStr

class ResumeCreate(ResumeBase):
    user_id: int

class ResumeOut(ResumeBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class ResumeFileOut(BaseModel):
    id: int
    file_url: HttpUrl
    uploaded_at: datetime

    class Config:
        orm_mode = True

class ResumeScoreOut(BaseModel):
    id: int
    metric: str
    value: str

    class Config:
        orm_mode = True
