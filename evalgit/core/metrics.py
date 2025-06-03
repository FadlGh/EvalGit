from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import json

def compute_metrics(y_true, y_pred):
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "f1": f1_score(y_true, y_pred, average="macro"),
        "precision": precision_score(y_true, y_pred, average="macro"),
        "recall": recall_score(y_true, y_pred, average="macro"),
    }

# Load from user files
with open("ground_truth.json") as f:
    y_true = json.load(f)["ground_truth"]

with open("predictions.json") as f:
    y_pred = json.load(f)["predictions"]

metrics = compute_metrics(y_true, y_pred)
print(metrics)
