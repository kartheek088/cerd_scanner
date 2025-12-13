import re
from scanner.entropy import shannon_entropy

PATTERNS = {
    "AWS_ACCESS_KEY": r'AKIA[0-9A-Z]{16}',
    "GENERIC_API_KEY": r'(?i)(api_key|apikey|secret|token)[\'"\s:=]{1,5}[A-Za-z0-9\-_=]{16,}',
    "JWT": r'eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+'
}

ENTROPY_THRESHOLD = 3.5

def detect_secrets(line):
    findings = []

    for secret_type, pattern in PATTERNS.items():
        matches = re.findall(pattern, line)
        for match in matches:
            entropy = shannon_entropy(match)
            if entropy >= ENTROPY_THRESHOLD:
                findings.append({
                    "type": secret_type,
                    "value": match,
                    "entropy": entropy
                })

    return findings
