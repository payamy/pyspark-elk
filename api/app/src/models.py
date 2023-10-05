import datetime

from sqlalchemy import *
from sqlalchemy.orm import relationship, Mapped, mapped_column

from typing import List

from .database import Base


class User(Base):

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(20), index=True, unique=True)
    name: Mapped[str] = mapped_column(String(20))
    signup_timestamp: Mapped[datetime.datetime]
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    visits: Mapped[List['Visit']] = relationship(back_populates='user')


class Visit(Base):

    __tablename__ = 'visits'

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    endpoint: Mapped[str] = mapped_column(String(50), index=True)
    query: Mapped[str] = mapped_column(String(200), index=True)
    visited_at: Mapped[datetime.datetime]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped['User'] = relationship(back_populates='visits')
