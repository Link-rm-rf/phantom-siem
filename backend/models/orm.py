from sqlalchemy import Column, Integer, String, Boolean, DateTime
from core.database import Base
from datetime import datetime

class DBLogEntry(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    source_ip = Column(String, index=True)
    event_type = Column(String, index=True)
    user_agent = Column(String, nullable=True)
    payload = Column(String)
    
    is_anomalous = Column(Boolean, default=False)
    threat_tags = Column(String, nullable=True)
