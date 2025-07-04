from fastapi import APIRouter, Response, Depends, HTTPException
from app.schemas.auth import UserLogin, UserCreate
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.schemas.user import UserPasswordUpdate
from db.db import get_db
from app.controller import user as crud
from app.controller.user import get_user_by_email, create_user
from app.services.hash import hash_password, verify_password


router = APIRouter()

@router.post("/login")
def login(user: UserLogin, response: Response, db : Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, details="Invalid Credentials")

    response.set_cookie(key="session_id", value=str(db_user.id))
    return {"message" : "User Logged in Successfully"}


@router.post("/signin")
def signin(user: UserCreate, db : Session = Depends(get_db)):
    exists = get_user_by_email(db, user.email)
    if exists:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user_data=user)
    

@router.get("/logout")
def logout(response : Response):
    response.delete_cookie("session_id")
    return {"message" : "User Logged out"}

@router.post("/update-password")
def update_password(password_data: UserPasswordUpdate, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, current_user.id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(password_data.current_password, user.password):
        raise HTTPException(status_code=401, detail="Invalid current password")

    user.password = hash_password(password_data.new_password)
    db.commit()
    db.refresh(user)
    return {"message": "Password updated successfully"}