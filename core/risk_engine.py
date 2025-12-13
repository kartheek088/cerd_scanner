from datetime import datetime

def calculate_risk(first_seen, occurrences):
    age_days = (datetime.utcnow() - datetime.fromisoformat(first_seen)).days
    risk = age_days * 2 + occurrences * 5
    return risk
