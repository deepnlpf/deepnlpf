#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

sentence = 'George Washington went to Washington.'

# path_dataset = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/data/dataset_1doc_1sent'
path_dataset = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/data/dataset_1doc_2sent'

path_pipeline = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/pipelines/json/flair.json'



nlp = Pipeline(_input=path_dataset, pipeline=path_pipeline, _output='file', boost='ray')

annotation = nlp.annotate()