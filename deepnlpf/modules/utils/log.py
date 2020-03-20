# -*- coding: utf-8 -*-
"""
    Path: /deepnlpf/util/
    File: log.py
    Description: 
    Date: 02/11/2019

    Types logging:
        logging.debug('This is a debug message')
        logging.info('This is an info message')
        logging.warning('This is a warning message')
        logging.error('This is an error message')
        logging.critical('This is a critical message')
"""
from deepnlpf.config import config
import logging
        
if config.DEBUG['log']:
    logging.basicConfig(
        # level=logging.DEBUG,
        filename=config.FILE['log'],
        filemode='w',
        format='%(asctime)s-%(process)d-%(levelname)s-%(message)s \n'
    )
