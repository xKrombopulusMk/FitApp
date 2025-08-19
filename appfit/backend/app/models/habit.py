from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from ..db.base import Base


class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    key = Column(String, nullable=False)
    target = Column(Integer, nullable=True)
    unit = Column(String, nullable=True)
    period = Column(String, nullable=True)
    streak = Column(Integer, default=0)
    last_check = Column(DateTime, nullable=True)
