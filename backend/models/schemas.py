from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class LogEntry(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    source_ip: str
    event_type: str
    user_agent: Optional[str] = None
    payload: str

    class Config:
        json_schema_extra = {
            "example": {
                "source_ip": "192.168.1.50",
                "event_type": "failed_login",
                "payload": "Failed password for root from 192.168.1.50 port 22"
            }
        }
