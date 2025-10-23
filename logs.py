import time
from pathlib import Path

LOGS_PATH = Path("logs")
LOGS_PATH.mkdir(parents=True, exist_ok=True)

def write_at_log(log_type: str, message: str):
    date = time.strftime("%Y-%m-%d")
    log_file = LOGS_PATH / f"log-{date}.log"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%H:%M:%S')}]|[{log_type.upper()}]: {message}\n")