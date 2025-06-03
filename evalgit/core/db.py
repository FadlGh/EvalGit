import os
import sqlite3

DB_PATH = os.path.join(os.path.expanduser("~"), ".evalgit", "metrics.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS evaluations (
            id TEXT PRIMARY KEY,
            timestamp TEXT,
            dataset TEXT,
            metrics_json TEXT,
            notes TEXT
        )
    """)
    conn.commit()
    conn.close()
