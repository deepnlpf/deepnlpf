#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Date: 25/03/2018
"""

import unittest
from deepnlpf.core.util import Dataset

class TestDataBase(unittest.TestCase):
    
    def __init__(self):
        pass

    def run(self):
        path_dataset = "/home/fasr/datasets/corpus_semval_2010"
        Dataset(path_dataset).save()

if __name__ == '__main__':
    unittest.main()