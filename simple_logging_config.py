"""
requirements.txt
better_exceptions==0.3.3 -> Show nice way the exepction (Optional)
python-decouple==3.8
python-json-logger==2.0.7
"""

## config.py
from decouple import config

APP_LOGGER = config("APP_LOGGER", default="AppLoggerName")
LOGLEVEL = config("LOG_LEVEL", default="INFO").upper()
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FORMAT = (
    "%(asctime)s - %(levelname)-8s - %(name)s - %(funcName)s - %(lineno)s - %(message)s"
    if LOGLEVEL == "DEBUG"
    else "%(asctime)s | %(levelname)-8s | %(message)s"
)

JSON_FORMAT_LOGGING = config("JSON_FORMAT_LOGGING", default=False, cast=bool)

LOGGING_CONF_DICT = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {"format": LOG_FORMAT, "datefmt": DATE_FORMAT},
        "json": {
            "format": LOG_FORMAT,
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
        },
    },
    "handlers": {
        # console logs to stderr
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "console_json": {"class": "logging.StreamHandler", "formatter": "json"},
    },
    "loggers": {
        # default for all undefined Python modules
        "": {
            "level": "DEBUG" if LOGLEVEL == "DEBUG" else "ERROR",
            "handlers": ["console_json" if JSON_FORMAT_LOGGING else "console"],
        },
        # Our application code
        APP_LOGGER: {
            "level": LOGLEVEL,
            "handlers": ["console_json" if JSON_FORMAT_LOGGING else "console"],
            # Avoid double logging because of root logger
            "propagate": False,
        },
        # avoid noisy logs
        "urllib3": {
            "level": "DEBUG" if LOGLEVEL == "DEBUG" else "ERROR",
            "handlers": ["console_json" if JSON_FORMAT_LOGGING else "console"],
        },
    },
}

## app.py

import config
import logging.config

logging.config.dictConfig(config.LOGGING_CONF_DICT)
log = logging.getLogger(config.APP_LOGGER)
log.info("Hello, Aladin-97")

