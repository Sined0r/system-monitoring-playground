import shutil
from utils.logger import log_result


def check_disk_usage(path: str = "/") -> dict:
    total, used, free = shutil.disk_usage(path)

    usage_percent = round((used / total) * 100, 2)

    status = "OK"
    if usage_percent > 90:
        status = "CRITICAL"
    elif usage_percent > 75:
        status = "WARNING"

    return {
        "path": path,
        "status": status,
        "usage_percent": usage_percent,
        "free_gb": round(free / (1024**3), 2)
    }


if name == "main":
    result = check_disk_usage()
    log_result(result)