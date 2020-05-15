#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

path_pipeline = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/unit/pipeline/custom_pipeline.json'
raw_text = 'I went to the bank to deposit my money.'

nlp = Pipeline(_input=raw_text, pipeline=path_pipeline, _output='file')
annotation = nlp.annotate()