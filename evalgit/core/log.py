from .io import load_json_array
from .metrics import compute_metrics
from .db import init_db, DB_PATH
from datetime import datetime, timezone
import sqlite3
import json 

def log_evaluation(model_name, gt_file, pred_file, dataset_name, notes=None):
    init_db()
    y_true = load_json_array(gt_file, key="ground_truth")
    y_pred = load_json_array(pred_file, key="predictions")
    metrics = compute_metrics(y_true, y_pred)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO evaluations (timestamp, model_name, dataset, metrics_json, notes) VALUES (?, ?, ?, ?, ?)",
        (datetime.now(timezone.utc).isoformat(), model_name, dataset_name, json.dumps(metrics), notes)
    )
    conn.commit()
    conn.close()
    return metrics
