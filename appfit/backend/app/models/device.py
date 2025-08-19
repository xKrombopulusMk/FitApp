from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON

from ..db.base import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    provider = Column(String, nullable=False)
    external_id = Column(String, nullable=False)
    access_token_enc = Column(String, nullable=True)
    refresh_token_enc = Column(String, nullable=True)
    scopes = Column(String, nullable=True)
    connected_at = Column(DateTime, default=datetime.utcnow)
