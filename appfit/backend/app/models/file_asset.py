from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from ..db.base import Base


class FileAsset(Base):
    __tablename__ = "file_assets"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    kind = Column(String, nullable=False)
    path = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
