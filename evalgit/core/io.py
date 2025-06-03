import os
import json

def load_json_array(path, key=None):
    abs_path = os.path.abspath(path)
    if not os.path.isfile(abs_path):
        raise FileNotFoundError(f"File not found: {abs_path}")

    with open(abs_path, "r") as f:
        data = json.load(f)

    if isinstance(data, list):
        return data
    if isinstance(data, dict) and key:
        if key in data:
            return data[key]
        raise KeyError(f"Key '{key}' not found in {abs_path}")
    raise ValueError(f"Unsupported JSON format in {abs_path}")
