from datetime import date
from sqlalchemy import Column, Integer, Float, Date, String, ForeignKey

from ..db.base import Base


class BodyComp(Base):
    __tablename__ = "bodycomp"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date, default=date.today)
    weight_kg = Column(Float, nullable=True)
    body_fat_pct = Column(Float, nullable=True)
    muscle_mass_kg = Column(Float, nullable=True)
    visceral_fat = Column(Float, nullable=True)
    notes = Column(String, nullable=True)
