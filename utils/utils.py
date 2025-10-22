import os
from datetime import datetime

def create_logger(log_dir="../logs", log_name="etl_log.txt"):
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_name)
    def log(message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_path, "a") as f:
            f.write(f"[{timestamp}] {message}\n")
        print(message)
    return log