from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON

from ..db.base import Base


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    level = Column(String, nullable=False)
    code = Column(String, nullable=False)
    message = Column(String, nullable=False)
    meta_json = Column(JSON, nullable=True)
    resolved_at = Column(DateTime, nullable=True)
