from pydantic import BaseModel, HttpUrl
from typing import Optional
from .enums import CompanySize

class CompanyBase(BaseModel):
    name: str
    industry: str
    location: str
    description: Optional[str] = None
    employee_count: Optional[int] = None
    size: CompanySize
    founded: Optional[int] = None
    website: Optional[HttpUrl] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyOut(CompanyBase):
    id: int

    class Config:
        orm_mode = True
