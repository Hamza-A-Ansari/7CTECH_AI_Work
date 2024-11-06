from src.lib.Liabraries import *
from src.helper.Config import get_config

def get_logger(logger_name, log_file="common.log"):
    """Creates a common logger

    Args:
        logger_name (str): Name of the logger.
        log_file (str): Name of the log file. Defaults to "common.log".

    Returns:
        logging.Logger: The configured logger object.
    """

    # Create logs directory if it doesn't exist
    log_dir = get_config('directories', 'logs_dir')
    os.makedirs(log_dir, exist_ok=True) 

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all log levels

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # File handler
    fh = logging.FileHandler(os.path.join(log_dir, log_file))
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Optionally add console output for debugging during development
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch) 

    return logger