from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON

from ..db.base import Base


class Badge(Base):
    __tablename__ = "badges"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    key = Column(String, nullable=False)
    earned_at = Column(DateTime, default=datetime.utcnow)
    meta_json = Column(JSON, nullable=True)
