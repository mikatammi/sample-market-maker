import logging
from datetime import datetime
from market_maker.settings import settings


def setup_custom_logger(name, log_level=settings.LOG_LEVEL):
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    datetimestring = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filehandler = logging.FileHandler("%s-%s.log" % (name, datetimestring))
    filehandler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    logger.addHandler(filehandler)
    return logger
