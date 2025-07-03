from fastapi import APIRouter
from routers import resume

router = APIRouter()
router.include_router(resume.router)
