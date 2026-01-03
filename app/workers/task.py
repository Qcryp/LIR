# app/workers/tasks.py
from celery import Celery
from app.connectors.wazuh import WazuhConnector
from app.services.ingest import ingest_wazuh_alerts

celery = Celery(
    "ir-worker",
    broker="redis://redis:6379/0"
)

@celery.task
def pull_wazuh_alerts():
    wazuh = WazuhConnector(
        url="https://wazuh-manager:55000",
        user="wazuh",
        password="password"
    )
    alerts = wazuh.fetch_alerts()
    ingest_wazuh_alerts(alerts)
