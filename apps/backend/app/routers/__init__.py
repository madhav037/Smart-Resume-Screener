from .user import router as user_router
# from .job import router as job_router
# from .resume import router as resume_router
# from .company import router as company_router
# from .application import router as application_router
from .auth import router as auth_router

__all__ = [
    "user_router",
    # "job_router",
    # "resume_router",
    # "company_router",
    # "application_router",
    "auth_router",
]
