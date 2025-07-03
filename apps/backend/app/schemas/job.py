from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .enums import EmploymentType, ApplicationStatus

class JobBase(BaseModel):
    title: str
    role: str
    location: str
    description: str
    requirements: Optional[str] = None
    responsibilities: Optional[str] = None
    salary_range: Optional[str] = None
    employment_type: EmploymentType
    open_positions: Optional[int] = None

class JobCreate(JobBase):
    company_id: int

class JobOut(JobBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True