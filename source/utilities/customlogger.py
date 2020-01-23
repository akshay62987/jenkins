import inspect
import logging
from venv import logger


def customLogger(logLevel=logging.DEBUG):
    # get the name of the class or method from where these are called
    loggerName = inspect.stack()[1][3]
    logger=logging.getLogger(loggerName)
    # by default.log all the messages
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s:%(message)s',datefmt='%m/%d/%y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
