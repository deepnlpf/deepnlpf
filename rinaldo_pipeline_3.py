#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

path_pipeline = '/home/fasr/datasets/08-04-2020/pipeline3.json'
path_dataset = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/data/semeval2010'

nlp = Pipeline(_input=path_dataset, pipeline=path_pipeline, _output='file', _format='xml', boost='ray')
annotation = nlp.annotate()