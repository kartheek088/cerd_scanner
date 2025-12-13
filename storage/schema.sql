CREATE TABLE IF NOT EXISTS secrets (
    id TEXT PRIMARY KEY,
    type TEXT,
    first_seen TEXT,
    last_seen TEXT,
    risk_score INTEGER
);

CREATE TABLE IF NOT EXISTS occurrences (
    secret_id TEXT,
    file_path TEXT,
    line_number INTEGER,
    FOREIGN KEY(secret_id) REFERENCES secrets(id)
);
