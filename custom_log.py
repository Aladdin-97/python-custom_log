__author__ = 'Aladin-29'
__version__ = '2.0'

import logging
from logging.handlers import RotatingFileHandler
import time

log = logging.getLogger()
consoleHandler = logging.StreamHandler()
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def custom_log_settings(logfile):
    """Set log format for file and console"""
    FILENAME = f'/path/to/logs/dir/{logfile}_{time.strftime("%Y%m%d")}.log'
    # Rotate File every 1GB,max 2 backup
    logfile_handler = RotatingFileHandler(filename=FILENAME, mode='a', encoding='utf-8', maxBytes=1000000000, backupCount=2)

    logfile_formatter = logging.Formatter(
        '%(asctime)s - %(filename)s - %(funcName)s - %(lineno)s - %(levelname)s - %(message)s', DATE_FORMAT)
    log.setLevel(logging.DEBUG)
    logfile_handler.setFormatter(logfile_formatter)
    # add the handlers to the log
    log.addHandler(logfile_handler)

    # logs  : print on screen
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', DATE_FORMAT)
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(console_formatter)
    log.addHandler(consoleHandler)
