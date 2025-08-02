import logging
import json
from datetime import datetime
import os
import glob

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

from dotenv import load_dotenv
load_dotenv()

MAX_LOGS = int(os.getenv("MAX_LOG_FILES", 20))

# Cleanup old logs: keep only the 20 most recent
def clean_old_logs(directory="logs", prefix="activity_", max_logs=20):
    files = sorted(glob.glob(os.path.join(directory, f"{prefix}*.log")), key=os.path.getmtime)
    while len(files) > max_logs:
        os.remove(files.pop(0))

# Create timestamped filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_filename = f"logs/activity_{timestamp}.log"

clean_old_logs(max_logs=MAX_LOGS)


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "message": record.getMessage(),
        }
        if hasattr(record, "extra"):
            log_record["data"] = record.extra
        return json.dumps(log_record)

# Create global logger
logger = logging.getLogger("kailash")
logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler(log_filename)
file_handler.setFormatter(JsonFormatter())
logger.addHandler(file_handler)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(JsonFormatter())
logger.addHandler(console_handler)

# Helper functions
def log_info(message, data=None):
    logger.info(message, extra={"extra": data or {}})

def log_error(message, data=None):
    logger.error(message, extra={"extra": data or {}})

def log_debug(message, data=None):
    logger.debug(message, extra={"extra": data or {}})

def log_warning(message, data=None):
    logger.warning(message, extra={"extra": data or {}})

def log_critical(message, data=None):
    logger.critical(message, extra={"extra": data or {}})

