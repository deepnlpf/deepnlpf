# -*- coding: utf-8 -*-

"""[logs]

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

    https://realpython.com/python-logging/
    https://realpython.com/python-time-module/
    https://github.com/reubano/pygogo
"""

# Quando for salvar os logs na base de dados usar isso:
# https://github.com/reubano/pygogo#json-formatter

import logging

import pygogo as gogo

from deepnlpf.global_parameters import HERE

log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(log_format)

logger = gogo.Gogo(
    "DeepNLPF",
    low_hdlr=gogo.handlers.file_hdlr(HERE+"/data.log"),
    low_formatter=formatter,
    high_level="error",
    high_formatter=formatter,
).logger
