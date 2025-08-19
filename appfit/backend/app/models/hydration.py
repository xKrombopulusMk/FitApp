from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey

from ..db.base import Base


class HydrationLog(Base):
    __tablename__ = "hydration_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    datetime = Column(DateTime, default=datetime.utcnow)
    ml = Column(Integer, nullable=False)
