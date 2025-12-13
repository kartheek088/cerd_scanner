# Secret Risk Tracker

A local-first tool that scans source code for exposed secrets and tracks
which ones remain risky over time, helping developers decide what to fix first.

---

## Why This Exists

Secret scanning tools already exist, but teams still miss critical leaks.
The problem is not detection — it is **prioritization**.

When many secrets are found:
- developers don’t know which ones matter
- alerts are ignored
- risky credentials remain exposed for long periods

This project focuses on **tracking and risk ranking**, not just scanning.

---

## What This Tool Does

- Scans a local codebase for potential secrets
- Detects secrets using pattern matching + entropy checks
- Fingerprints secrets (hash-based, no raw secrets stored)
- Tracks secrets across multiple runs
- Ranks secrets based on risk factors such as age and recurrence
- Outputs a clear CLI report highlighting what needs attention

---

## What This Tool Does NOT Do

This project intentionally does **not**:
- rotate or revoke secrets
- integrate with cloud providers
- provide a hosted service or SaaS
- use machine learning
- claim to prevent breaches

It is a focused analysis and prioritization tool.

---

## How It Works (High Level)

1. Walks through files in a given directory
2. Detects potential secrets using regex patterns
3. Filters false positives using entropy scoring
4. Generates a fingerprint for each secret
5. Stores secret metadata in a local SQLite database
6. Tracks first seen, last seen, and occurrences
7. Calculates a simple risk score
8. Outputs a rank
