from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from ..db.base import Base


class Quest(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    period = Column(String, nullable=True)
    status = Column(String, default="pending")
    xp_reward = Column(Integer, default=0)
