from datetime import datetime, date
from sqlalchemy import Column, Integer, String, Date, DateTime, JSON

from ..db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    name = Column(String, nullable=True)
    sex = Column(String, nullable=True)
    birthdate = Column(Date, nullable=True)
    height_cm = Column(Integer, nullable=True)
    preferences_json = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
