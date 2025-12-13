import sys
from scanner.file_scanner import scan_files
from scanner.detectors import detect_secrets
from core.fingerprint import fingerprint_secret
from core.risk_engine import calculate_risk
from storage.database import init_db, upsert_secret, add_occurrence, fetch_secrets
from reports.cli_output import print_report

def main(path):
    init_db()

    for file_path, line_no, line in scan_files(path):
        findings = detect_secrets(line)

        for finding in findings:
            secret_id = fingerprint_secret(finding["value"])
            upsert_secret(secret_id, finding["type"])
            add_occurrence(secret_id, file_path, line_no)

    secrets = fetch_secrets()

    enriched = []
    for s in secrets:
        risk = calculate_risk(s[2], s[4])
        enriched.append((s[0], s[1], s[2], s[4], risk))

    print_report(enriched)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_codebase>")
        sys.exit(1)

    main(sys.argv[1])
