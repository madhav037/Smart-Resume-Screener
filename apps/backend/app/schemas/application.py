from pydantic import BaseModel
from datetime import datetime
from .enums import ApplicationStatus

class ApplicationBase(BaseModel):
    user_id: int
    job_id: int
    resume_id: int

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationOut(ApplicationBase):
    id: int
    status: ApplicationStatus
    applied_at: datetime

    class Config:
        orm_mode = True

class StatusHistoryOut(BaseModel):
    id: int
    application_id: int
    old_status: str
    new_status: str
    updated_at: datetime
    updated_by: int

    class Config:
        orm_mode = True