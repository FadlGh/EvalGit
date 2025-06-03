import os
import sqlite3
from platformdirs import user_data_dir
from pathlib import Path

appname = "EvalGit"
DB_PATH = Path(user_data_dir(appname)) / "evaluations.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS evaluations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            model_name TEXT,
            dataset TEXT,
            metrics_json TEXT,
            notes TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_all_evaluations():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM evaluations ORDER BY timestamp;").fetchall()
    conn.close()
    return rows

def get_specific_row(key, value):
    allowed_keys = {"id", "timestamp", "model_name", "dataset", "notes"}
    if key not in allowed_keys:
        raise ValueError(f"Invalid key: {key}. Allowed keys are: {allowed_keys}")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = f"SELECT * FROM evaluations WHERE {key} = ? LIMIT 1;"
    cursor.execute(query, (value,))
    row = cursor.fetchone()
    conn.close()
    return row

def delete_all_rows():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM evaluations;")
    conn.commit()
    conn.close()

def delete_specific_row(key, value):
    allowed_keys = {"id", "timestamp", "model_name", "dataset", "notes"}
    if key not in allowed_keys:
        raise ValueError(f"Invalid key: {key}. Allowed keys are: {allowed_keys}")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM evaluations WHERE {key} = ?;", (value,))
    conn.commit()
    conn.close()