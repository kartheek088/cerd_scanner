import hashlib

def fingerprint_secret(secret_value):
    return hashlib.sha256(secret_value.encode()).hexdigest()
