# app/services/ingest.py
from app.db.session import SessionLocal
from app.db.models import Alert

def ingest_wazuh_alerts(alerts):
    db = SessionLocal()
    for a in alerts:
        alert = Alert(
            source="wazuh",
            source_alert_id=a.get("id"),
            severity=a["rule"]["level"],
            title=a["rule"]["description"],
            host=a["agent"]["name"],
            ip=a["data"].get("srcip"),
            user=a["data"].get("user"),
            raw=a
        )
        db.add(alert)
    db.commit()
    db.close()
