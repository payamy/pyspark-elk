from sqlalchemy.orm import Session

from ..models import User
from ..schemas import UserCreate
from ..security import pwd_context

import datetime


def get_user(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    user_model = User(
        signup_timestamp=datetime.datetime.now(),
        hashed_password=hashed_password,
        username=user.username,
        name=user.name,
    )
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return user_model
