from sqlalchemy.orm import Session

from ..models import Visit, User
from ..schemas import VisitCreate

import datetime


def get_visits(db: Session, user_id: int) -> Visit:
    return db.query(Visit).filter(Visit.user_id == user_id).first()


def create_visit_record(db: Session, user_id: int, visit: VisitCreate):
    visit_obj = Visit(
        visited_at=datetime.datetime.now(),
        user_id=user_id,
        endpoint=visit.endpoint,
        query=visit.query,
    )
    db.add(visit_obj)
    db.commit()
    db.refresh(visit_obj)
    return visit_obj
