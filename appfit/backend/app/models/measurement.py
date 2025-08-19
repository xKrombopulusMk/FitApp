from datetime import date
from sqlalchemy import Column, Integer, Float, Date, ForeignKey

from ..db.base import Base


class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date, default=date.today)
    steps = Column(Integer, nullable=True)
    hr_avg = Column(Integer, nullable=True)
    hr_rest = Column(Integer, nullable=True)
    vo2max_est = Column(Float, nullable=True)
    calories_burned = Column(Integer, nullable=True)
