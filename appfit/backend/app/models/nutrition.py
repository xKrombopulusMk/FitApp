from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey, JSON

from ..db.base import Base


class NutritionLog(Base):
    __tablename__ = "nutrition_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    datetime = Column(DateTime, default=datetime.utcnow)
    items_json = Column(JSON, nullable=True)
    calories = Column(Integer, nullable=True)
    protein_g = Column(Float, nullable=True)
    carbs_g = Column(Float, nullable=True)
    fat_g = Column(Float, nullable=True)
    fiber_g = Column(Float, nullable=True)
    sodium_mg = Column(Float, nullable=True)
    source = Column(String, nullable=True)
