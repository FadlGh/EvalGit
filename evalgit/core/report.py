import os
from datetime import datetime
from platformdirs import user_data_dir
from pathlib import Path

def write_report(model_name, metrics, dataset, notes, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

    appname = "EvalGit"
    reports_dir = Path(user_data_dir(appname)) / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    path = reports_dir / f"{model_name}_{timestamp}.md"

    # Determine column widths
    metric_col_width = max(len("Metric"), max(len(k.capitalize()) for k in metrics.keys()))
    value_col_width = max(len("Value"), max(len(f"{v:.4f}") for v in metrics.values()))

    # Format header and separator with dynamic width
    header = f"| {'Metric'.ljust(metric_col_width)} | {'Value'.ljust(value_col_width)} |"
    separator = f"|{'-' * (metric_col_width + 2)}|{'-' * (value_col_width + 2)}|"

    # Format metric rows
    metric_lines = "\n".join(
        f"| {k.capitalize().ljust(metric_col_width)} | {f'{v:.4f}'.ljust(value_col_width)} |"
        for k, v in metrics.items()
    )

    content = f"""# EvalGit Report

**Model Name:** `{model_name}`  
**Timestamp:** `{timestamp}`  
**Dataset:** `{dataset}`  
**Notes:** {notes}

---

## 📊 Metrics

{header}  
{separator}  
{metric_lines}

---

✅ Logged via EvalGit
"""

    with open(path, "w") as f:
        f.write(content)

    return path
