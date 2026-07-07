import json
import logging
import logging.config
import logging.handlers
import os
from datetime import UTC, datetime
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

_ENV = os.getenv("ENV", "development")
_LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG" if _ENV == "development" else "INFO")

_PACKAGES = ["agents", "app", "ingestion", "llm", "rag", "tools", "evaluation"]


class _JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        entry: dict[str, object] = {
            "timestamp": datetime.now(UTC).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        if record.exc_info:
            entry["exception"] = self.formatException(record.exc_info)
        if record.stack_info:
            entry["stack"] = self.formatStack(record.stack_info)
        return json.dumps(entry)


_LOGGING_CONFIG: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s | %(levelname)-8s | %(name)-30s | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "json": {
            "()": _JSONFormatter,
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard" if _ENV == "development" else "json",
            "stream": "ext://sys.stdout",
            "level": _LOG_LEVEL,
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "json",
            "filename": str(LOG_DIR / "app.log"),
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 5,
            "encoding": "utf-8",
            "level": _LOG_LEVEL,
        },
        "error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "json",
            "filename": str(LOG_DIR / "errors.log"),
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 5,
            "encoding": "utf-8",
            "level": "ERROR",
        },
    },
    "loggers": {
        pkg: {
            "level": _LOG_LEVEL,
            "handlers": ["console", "file", "error_file"],
            "propagate": False,
        }
        for pkg in _PACKAGES
    },
    "root": {
        "level": "WARNING",
        "handlers": ["console", "error_file"],
    },
}


def setup_logging() -> None:
    """Call once at application startup (e.g. in FastAPI lifespan or main)."""
    logging.config.dictConfig(_LOGGING_CONFIG)


def get_logger(name: str) -> logging.Logger:
    """Return a logger scoped to *name* (typically __name__)."""
    return logging.getLogger(name)
