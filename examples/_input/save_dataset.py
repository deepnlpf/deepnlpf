#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.dataset import Dataset

path_dataset = ''
result = Dataset().save(path_dataset)
print(result)