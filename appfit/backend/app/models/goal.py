from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey

from ..db.base import Base


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String, nullable=False)
    target_value = Column(Float, nullable=True)
    unit = Column(String, nullable=True)
    deadline = Column(DateTime, nullable=True)
    status = Column(String, default="active")
