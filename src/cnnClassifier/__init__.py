import os
import logging
import sys

log_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
file_path = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)  # Create directory if it doesn't exist

logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    handlers=[
        logging.FileHandler(file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")
