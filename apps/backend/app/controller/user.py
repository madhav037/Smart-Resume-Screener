from sqlalchemy.orm import Session
from app.db.models import User
from app.schemas import UserCreate, UserOut

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    return db.query(User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user_data: dict) -> User | None:
    user = get_user_by_id(db, user_id)
    if user:
        for key, value in user_data.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user
    return None

def delete_user(db: Session, user_id: int) -> User | None:
    user = get_user_by_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user