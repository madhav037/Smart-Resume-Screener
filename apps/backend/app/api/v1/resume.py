from fastapi import APIRouter
from db import get_connection

router = APIRouter()

@router.get("/resumes")
def list_resumes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, score FROM resumes")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1], "email": r[2], "score": r[3]} for r in data]