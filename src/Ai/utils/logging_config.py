# ai/utils/logging_config.py
import logging
import sys

def setup_logging():
    """
    Configures logging for the entire application.
    Logs to the console with a specific format.
    """
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    if root_logger.handlers:
        root_logger.handlers = []

    # This handles logging in the console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG) # You can set a different level here if needed
    # This will format the log messages using the specified format
    formatter = logging.Formatter(log_format)
    console_handler.setFormatter(formatter)

    # Add the handler to the root logger
    root_logger.addHandler(console_handler)

    print("Logging configured.")