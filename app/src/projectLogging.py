import logging


class ProjectLogging:

    logger = logging.getLogger("fastapi")
    logger.setLevel(logging.getLevelName(logging.INFO))
    log_handler = logging.StreamHandler()
    log_format = logging.Formatter("{%(asctime)s} [%(levelname)s]: %(message)s")
    log_handler.setFormatter(log_format)
    logger.addHandler(log_handler)