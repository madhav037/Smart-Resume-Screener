from fastapi import FastAPI
from api.v1 import router as v1_router
from db import init_db
from dotenv import load_dotenv
import os

load_dotenv()

api_version = os.getenv("API_VERSION")
prefix= f"/api/{api_version}"

app = FastAPI()
init_db()

app.include_router(v1_router, prefix=prefix)
