from core.io import load_json_array
from core.metrics import compute_metrics

y_true = load_json_array("test_data/ground_truth.json", key="ground_truth")
y_pred = load_json_array("test_data/predictions.json", key="predictions")
metrics = compute_metrics(y_true, y_pred)
print(metrics)
