#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

path_pipeline = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/pipelines/json/pipeline_flair.json'
sentence = 'George Washington went to Washington.'

nlp = Pipeline(
    _input=sentence, 
    pipeline=path_pipeline, 
    _output='file', 
    boost='ray')

annotation = nlp.annotate()