#!/usr/bin/env python3

from collections import Counter
from typing import Dict

def log_counter(logs: str) -> Dict[str, int]:
    errors = []
    for line in logs.splitlines():
        if "ERROR" in line:
            errors.append(line.split("ERROR", 1)[1].strip())
    return dict(Counter(errors))


if __name__ == "__main__":
    logs = """
[2025-07-08 10:01:23] INFO Server started
[2025-07-08 10:01:45] ERROR Connection timeout
[2025-07-08 10:02:02] ERROR Connection timeout
[2025-07-08 10:03:00] ERROR Disk full
"""
    print(log_counter(logs))
