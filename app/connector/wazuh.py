# app/connectors/wazuh.py
import requests

class WazuhConnector:
    def __init__(self, url, user, password):
        self.url = url
        self.auth = (user, password)

    def fetch_alerts(self, severity_min=10):
        endpoint = f"{self.url}/security/events"
        params = {
            "limit": 50,
            "q": f"rule.level>={severity_min}"
        }

        r = requests.get(endpoint, auth=self.auth, params=params, verify=False)
        r.raise_for_status()
        return r.json()["data"]["affected_items"]
