# app/main.py
from fastapi import FastAPI
from app.api import alerts

app = FastAPI(title="IR Orchestrator")

app.include_router(alerts.router)
