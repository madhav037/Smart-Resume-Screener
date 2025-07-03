from sqlalchemy import Column, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from app.db.db import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    location = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    employee_count = Column(Integer, nullable=True)
    size = Column(Enum("small", "medium", "large", name="company_size"), nullable=False)
    founded = Column(Integer, nullable=True)
    website = Column(String, nullable=True)

    job_descriptions = relationship("JobDescription", back_populates="company")
    admins = relationship("CompanyAdmin", back_populates="company")