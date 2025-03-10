import os
import sys
import logging

# create logging string
logging_str = "[%(asctime)%s: %(levelname)s: %(module)s: %(message)s]"

# creating logging folder name
log_dir = "logs"

# creating the logging file and joining it with the folder name
log_filepath = os.path.join(log_dir, "running_logs.log")

# creating the folder
os.makedirs(log_filepath, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)  # print to console too
    ]
)

logger = logging.getLogger("mlProjectLogger")