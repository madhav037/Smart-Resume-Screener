from pydantic import BaseModel
from typing import List

class SkillBase(BaseModel):
    name: str

class SkillCreate(SkillBase):
    pass

class SkillOut(SkillBase):
    id: int

    class Config:
        orm_mode = True


class UserSkillCreate(BaseModel):
    user_id: int
    skill_ids: List[int]  # You can bulk insert from frontend
