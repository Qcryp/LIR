# app/db/models.py
from sqlalchemy import Column, Integer, String, DateTime, JSON
from app.db.base import Base
from datetime import datetime

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)
    source = Column(String)
    source_alert_id = Column(String)
    severity = Column(Integer)
    title = Column(String)
    host = Column(String)
    ip = Column(String)
    user = Column(String)
    raw = Column(JSON)
    status = Column(String, default="open")
    created_at = Column(DateTime, default=datetime.utcnow)
