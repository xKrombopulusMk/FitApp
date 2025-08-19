from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey, JSON

from ..db.base import Base


class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    source = Column(String, nullable=True)
    type = Column(String, nullable=True)
    start = Column(DateTime, default=datetime.utcnow)
    duration_min = Column(Float, nullable=True)
    distance_km = Column(Float, nullable=True)
    calories = Column(Integer, nullable=True)
    avg_hr = Column(Integer, nullable=True)
    data_json = Column(JSON, nullable=True)
