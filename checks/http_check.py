import requests
import time
from utils.logger import log_result


def check_service(url: str, timeout: float = 3.0) -> dict:
    start_time = time.time()

    try:
        response = requests.get(url, timeout=timeout)
        elapsed = round((time.time() - start_time) * 1000, 2)

        result = {
            "service": url,
            "status": "UP" if response.status_code == 200 else "DEGRADED",
            "http_status": response.status_code,
            "response_time_ms": elapsed
        }

    except requests.RequestException as e:
        result = {
            "service": url,
            "status": "DOWN",
            "error": str(e)
        }

    return result


if name == "main":
    result = check_service("https://google.com")
    log_result(result)