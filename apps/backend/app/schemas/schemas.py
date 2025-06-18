from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, JSON
from typing import Optional, List
from uuid import uuid4
from enum import Enum
import datetime


class Role(str, Enum):
    admin = "admin"
    owner = "owner"
    manager = "manager"
    recruiter = "recruiter"


class User(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    email: str = Field(index=True, unique=True)
    password: str
    name: str
    role: Role
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

    jobs: List["Job"] = Relationship(back_populates="created_by_user")


class Company(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    name: str
    created_by: str = Field(foreign_key="user.id")
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class Job(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    title: str
    description: str
    department: str
    location: str
    is_remote: bool
    salary_min: Optional[int]
    salary_max: Optional[int]

    company_id: str = Field(foreign_key="company.id")
    created_by_id: str = Field(foreign_key="user.id")

    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

    created_by_user: Optional[User] = Relationship(back_populates="jobs")
    requirements: List["JobRequirement"] = Relationship(back_populates="job")

class RequirementType(str, Enum):
    skill = "skill"
    education = "education"
    language = "language"
    experience = "experience"
    certification = "certification"
    knockout = "knockout"


class JobRequirement(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    job_id: str = Field(foreign_key="job.id")
    type: RequirementType
    value: str
    weight: int
    required: bool = False

    job: Job = Relationship(back_populates="requirements")


class Resume(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    job_id: str = Field(foreign_key="job.id")
    uploaded_by: str = Field(foreign_key="user.id")
    file_url: str
    parsed_json: Optional[dict] = Field(default_factory=dict, sa_column=Column(JSON))
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)


class ResumeScore(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    resume_id: str = Field(foreign_key="resume.id")
    overall_score: int
    skills_score: Optional[int]
    experience_score: Optional[int]
    education_score: Optional[int]
    cultural_fit: Optional[int]
    confidence: Optional[float]
    explanation: Optional[str]
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)


class ReviewNote(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    resume_id: str = Field(foreign_key="resume.id")
    user_id: str = Field(foreign_key="user.id")
    note: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
