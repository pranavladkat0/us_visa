import logging
import os
from from_root import from_root
from datetime import datetime

# Create log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = "logs"
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

# Create directory properly
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# Create logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# 🔥 Prevent duplicate logs
if not logger.handlers:

    # File handler
    file_handler = logging.FileHandler(logs_path)
    file_handler.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Format
    formatter = logging.Formatter(
        "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Test log
logger.info("Logging started successfully")