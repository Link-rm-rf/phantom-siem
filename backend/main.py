from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models.schemas import LogEntry
from models.orm import DBLogEntry
from core.detection import detector
from core.database import engine, Base, get_db
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("phantom-siem")

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Phantom-SIEM API", version="1.0.0")

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/ingest")
async def ingest_log(log: LogEntry, db: Session = Depends(get_db)):
    try:
        analysis = detector.scan_payload(log.payload)
        
        db_log = DBLogEntry(
            source_ip=log.source_ip,
            event_type=log.event_type,
            user_agent=log.user_agent,
            payload=log.payload,
            is_anomalous=analysis["is_anomalous"],
            threat_tags=",".join(analysis["threat_tags"]) if analysis["threat_tags"] else None
        )
        db.add(db_log)
        db.commit()
        db.refresh(db_log)
        
        if analysis["is_anomalous"]:
            logger.warning(f"🚨 THREAT SAVED from {log.source_ip}: {analysis['threat_tags']}")
            
        return {"status": "success", "log_id": db_log.id, "anomalies": analysis["is_anomalous"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Fetch logs 
@app.get("/api/v1/logs")
async def get_logs(limit: int = 50, db: Session = Depends(get_db)):
    logs = db.query(DBLogEntry).order_by(DBLogEntry.id.desc()).limit(limit).all()
    return logs
