__author__ = 'Aladin-97'
__version__ = '1.0'

import time
import logging
from logging.handlers import RotatingFileHandler


log = logging.getLogger()
consoleHandler = logging.StreamHandler()
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def custom_log_settings(
    logs_dir_path, logfile, console_log_level=logging.INFO, file_log_level=logging.DEBUG
):
    """Set log format for file and console"""
    FILENAME = f'{logs_dir_path}/{logfile}_{time.strftime("%Y%m%d")}.log'
    # Rotate File every 1GB,max 2 backup
    logfile_handler = RotatingFileHandler(
        filename=FILENAME,
        mode="a",
        encoding="utf-8",
        maxBytes=1000000000,
        backupCount=2,
    )

    logfile_formatter = logging.Formatter(
        "%(asctime)s - %(filename)s - %(funcName)s - %(lineno)s - %(levelname)s - %(message)s",
        DATE_FORMAT,
    )
    log.setLevel(file_log_level)
    logfile_handler.setFormatter(logfile_formatter)
    # add the handlers to the log
    log.addHandler(logfile_handler)

    # logs  : print on screen
    console_formatter = logging.Formatter(
        # "%(asctime)s - %(levelname)s: %(message)s", DATE_FORMAT
        "[%(levelname)s]: %(message)s"
    )
    consoleHandler.setLevel(console_log_level)
    consoleHandler.setFormatter(console_formatter)
    log.addHandler(consoleHandler)
