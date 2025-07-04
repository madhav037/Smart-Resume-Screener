from fastapi import FastAPI
from app.routers import (
    user_router,
    # job_router,
    # resume_router,
    # company_router,
    # application_router,
    auth_router,
)
from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI()
prefix = f"/api/{os.getenv('API_VERSION') or 'v1'}"

app.include_router(auth_router, prefix=f"{prefix}/auth")
app.include_router(user_router, prefix=f"{prefix}/users")
# app.include_router(job_router, prefix=f"{prefix}/jobs")
# app.include_router(resume_router, prefix=f"{prefix}/resumes")
# app.include_router(company_router, prefix=f"{prefix}/companies")
# app.include_router(application_router, prefix=f"{prefix}/applications")
