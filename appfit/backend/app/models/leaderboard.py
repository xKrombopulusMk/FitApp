from datetime import date
from sqlalchemy import Column, Integer, Date, ForeignKey

from ..db.base import Base


class LeaderboardDaily(Base):
    __tablename__ = "leaderboard_daily"

    id = Column(Integer, primary_key=True)
    date = Column(Date, default=date.today)
    user_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Integer, default=0)
    rank = Column(Integer, default=0)
