#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

sentence = 'I went to the bank to deposit my money.'

path_pipeline = '/home/fasr/Mestrado/deepnlpf/examples/pipelines/json/pywsd.json'

nlp = Pipeline(_input=sentence, pipeline=path_pipeline, _output='file')
annotation = nlp.annotate()