#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

path_pipeline = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/pipelines/json/banchmarking_boost.json'

raw_text = 'I went to the bank to deposit my money.'
document = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/data/banchmarking'

nlp = Pipeline(_input=raw_text, pipeline=path_pipeline, _output='file', boost='ray')
annotation = nlp.annotate()