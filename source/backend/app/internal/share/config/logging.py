logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "json_ensure_ascii": False,
        }
    },
    "handlers": {"default": {"class": "logging.StreamHandler", "formatter": "default"}},
    "root": {"handlers": ["default"], "level": "INFO"},
}
