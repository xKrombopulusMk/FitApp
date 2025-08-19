from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, JSON

from ..db.base import Base


class SleepLog(Base):
    __tablename__ = "sleep_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    start = Column(DateTime, default=datetime.utcnow)
    end = Column(DateTime, default=datetime.utcnow)
    duration_min = Column(Integer, nullable=True)
    stages_json = Column(JSON, nullable=True)
    quality_score = Column(Float, nullable=True)
