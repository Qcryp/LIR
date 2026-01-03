# app/connectors/base.py
class BaseConnector:
    def fetch_alerts(self):
        raise NotImplementedError
