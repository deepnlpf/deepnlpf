#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

sentence = 'The human brain is quite proficient at word-sense disambiguation.'
path_dataset = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/data/dataset_1doc_2sent'

path_pipeline = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/pipelines/json/supwsd.json'

nlp = Pipeline(_input=path_dataset, pipeline=path_pipeline, _output='file',boost='ray')
annotation = nlp.annotate()
