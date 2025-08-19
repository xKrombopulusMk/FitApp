from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from ..db.base import Base


class Consent(Base):
    __tablename__ = "consents"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    scope = Column(String, nullable=False)
    granted_at = Column(DateTime, default=datetime.utcnow)
    revoked_at = Column(DateTime, nullable=True)
