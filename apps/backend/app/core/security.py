from fastapi import HTTPException, Request, Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.db.models.user import User

def get_current_user(request : Request, db : Session = Depends(get_db)) -> User:
    session_id = request.cookies.get("session_id")
    if not session_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user = db.query(User).filter(User.id == session_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid session") 
    
    return user

def require_role(required_role: str):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(status_code=403, detail="Forbidden: Insufficient role")
        return current_user
    return role_checker