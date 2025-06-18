from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://resume_user:resume_pass@db:5432/resume_screener"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session