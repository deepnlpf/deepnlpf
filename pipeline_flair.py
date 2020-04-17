#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

path_pipeline = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/piplines/json/pipeline_flair.json'
sentence = 'The grass is green.'

nlp = Pipeline(_input=sentence, pipeline=path_pipeline)
annotation = nlp.annotate()