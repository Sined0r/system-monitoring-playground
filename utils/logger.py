import json
from datetime import datetime


def log_result(data: dict):
    timestamp = datetime.utcnow().isoformat()

    entry = {
        "timestamp": timestamp,
        "data": data
    }

    print(json.dumps(entry, indent=2))

    with open("logs/monitor.log", "a") as f:
        f.write(json.dumps(entry) + "\n")