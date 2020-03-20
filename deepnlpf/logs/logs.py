# -*- coding: utf-8 -*-
"""[logs]

    https://realpython.com/python-logging/

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

    # Tutorial: https://realpython.com/python-time-module/
"""
import os
import sys
import logging
import pygogo as gogo

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
#os.environ.update({'ROOT_PATH': ROOT_PATH})
#sys.path.append(os.path.join(ROOT_PATH, 'logs'))

DEBUG = True

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(log_format)

logger = gogo.Gogo(
    'deepnlf.',
    low_hdlr=gogo.handlers.file_hdlr('data.log'),
    low_formatter=formatter,
    high_level='error',
    high_formatter=formatter).logger
