from checks.http_check import check_service
from checks.disk_check import check_disk_usage
from utils.logger import log_result


def run_all_checks():
    results = []

    # HTTP check
    results.append(check_service("https://google.com"))

    # Disk check
    results.append(check_disk_usage("/"))

    return results


if name == "main":
    all_results = run_all_checks()

    for result in all_results:
        log_result(result)