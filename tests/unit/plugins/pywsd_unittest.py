#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

path_pipeline = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/pipelines/json/pywsd.json'
sentence = 'I went to the bank to deposit my money.'

nlp = Pipeline(_input=sentence, pipeline=path_pipeline, _output='file', boost='ray')
annotation = nlp.annotate()