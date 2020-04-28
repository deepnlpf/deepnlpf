#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from deepnlpf.pipeline import Pipeline

sentence = "I went to the bank to deposit my money."
path_pipeline = ''

nlp = Pipeline(_input=sentence, pipeline=path_pipeline, _output='file', boost='ray')

annotation = nlp.annotate()
