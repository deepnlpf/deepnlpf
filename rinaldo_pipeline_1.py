#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

path_pipeline = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/data/pipeline1.json'
path_dataset = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/data/semeval2010'

nlp = Pipeline(_input=path_dataset, pipeline=path_pipeline, _output='file', _format='xml')
annotation = nlp.annotate()