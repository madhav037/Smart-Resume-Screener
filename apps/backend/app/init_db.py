# init_db.py
from sqlmodel import SQLModel
from db import engine

from schemas.schemas import User, Company, Job, JobRequirement, Resume, ResumeScore, ReviewNote

def init_db():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()