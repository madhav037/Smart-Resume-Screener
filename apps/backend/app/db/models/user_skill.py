from sqlalchemy import Column, Integer, ForeignKey
from app.db.db import Base

class UserSkill(Base):
    __tablename__ = "user_skills"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    skill_id = Column(Integer, ForeignKey("skills.id"))
