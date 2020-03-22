# -*- coding: utf-8 -*-

'''
    Path: /deepnlpf/config/
    File: config.py
    Description: 
        In this file, you will find some settings that need to be adjusted before you 
        start using this tool, you will find here things like external NLP tool path 
        configuration and some of the usage settings, check the documentation for more 
        details.
    Date: 03/07/2018
'''

import os, pathlib


HOME = os.environ['HOME']
PATH_BASE = str(pathlib.Path.cwd())
NLPTOOLS = "/nlptools/"

DEBUG = {
    'log': False,
}

LANG = {
    'lang': 'en'
}

PATH = {
    'path_root': PATH_BASE,
    'path_dir_temp': PATH_BASE + '/deepnlpf/tmp',
}

FILE = {
    'xsd': 'scheme.xsd',
    'temp_tokens': 'tmp-tokens-scnlp.txt',
    'xwnd': str(pathlib.Path.cwd()) + '/resources/dict/xwnd-30g/',
    'log': str(pathlib.Path.cwd()) + '/deepnlpf/logs/data.log',
}
