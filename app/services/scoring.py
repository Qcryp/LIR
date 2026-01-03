# app/services/scoring.py

RISK_LEVELS = {
    "CRITICAL": 80,
    "HIGH": 60,
    "MEDIUM": 40
}

ASSET_CRITICALITY = {
    "domain_controller": 40,
    "database": 35,
    "production_app": 30,
    "bastion": 30,
    "user_endpoint": 15,
    "test_server": 5
}

def calculate_risk(alert, asset_type="user_endpoint", recurrence=0):
    score = 0

    # 1. Severity
    severity = alert.severity
    score += severity * 2  # weight

    # 2. Asset Criticality
    score += ASSET_CRITICALITY.get(asset_type, 10)

    # 3. Context bonus
    if recurrence >= 3:
        score += 10

    if "ransomware" in alert.title.lower():
        score += 20

    if alert.user and alert.user.lower() in ["administrator", "root"]:
        score += 10

    return score
