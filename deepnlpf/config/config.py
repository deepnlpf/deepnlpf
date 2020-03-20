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

CONFIG = {
    'host': '127.0.0.1',
    'port_server': 5000,
    'port_dashboard': 5001,
}

DEBUG = {
    'log': False,
}

LANG = {
    'lang': 'en'
}

PATH = {
    'path_root': PATH_BASE,
    'path_dir_temp': PATH_BASE + '/deepnlpf/tmp',
    'path_dir_stanford_corenlp': HOME + NLPTOOLS + 'stanford-corenlp-full-2018-10-05/',
    'path_dir_semafor': HOME + NLPTOOLS + 'semafor/',
    'path_dir_cogcomp_nlp': HOME + NLPTOOLS + 'cogcomp-nlp/',
    'path_dir_gate': PATH_BASE + '/resources/dict/gazetteer-gate-8.5.1/',
    'path_dir_wnd': PATH_BASE + '/resources/dict/wnd-3.2/',
    'path_dir_asumo': PATH_BASE + '/resources/dict/AS26WN30Mapping/',
    'path_supwsd': HOME + NLPTOOLS + 'supwsd/',
}

FILE = {
    'xsd': 'scheme.xsd',
    'temp_tokens': 'tmp-tokens-scnlp.txt',
    'xwnd': str(pathlib.Path.cwd()) + '/resources/dict/xwnd-30g/',
    'log': str(pathlib.Path.cwd()) + '/deepnlpf/logs/data.log',
    'tmp_in_semafor': 'tmp-in-semafor.txt',
    'tmp_out_semafor': 'tmp-out-semafor.txt',
}
