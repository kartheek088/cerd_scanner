import sqlite3
from datetime import datetime

DB_NAME = "secrets.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    with open("storage/schema.sql") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

def upsert_secret(secret_id, secret_type):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    now = datetime.utcnow().isoformat()

    cur.execute("SELECT id FROM secrets WHERE id=?", (secret_id,))
    exists = cur.fetchone()

    if exists:
        cur.execute(
            "UPDATE secrets SET last_seen=? WHERE id=?",
            (now, secret_id)
        )
    else:
        cur.execute(
            "INSERT INTO secrets (id, type, first_seen, last_seen, risk_score) VALUES (?, ?, ?, ?, 0)",
            (secret_id, secret_type, now, now)
        )

    conn.commit()
    conn.close()

def add_occurrence(secret_id, file_path, line_number):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO occurrences (secret_id, file_path, line_number) VALUES (?, ?, ?)",
        (secret_id, file_path, line_number)
    )

    conn.commit()
    conn.close()

def fetch_secrets():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        SELECT s.id, s.type, s.first_seen, s.last_seen,
               COUNT(o.file_path) as occurrences
        FROM secrets s
        LEFT JOIN occurrences o ON s.id = o.secret_id
        GROUP BY s.id
    """)

    rows = cur.fetchall()
    conn.close()
    return rows
