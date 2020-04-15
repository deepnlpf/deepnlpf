#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

path_pipeline = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/unit/pipeline/custom_pipeline.json'
path_dataset = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/data/dataset_1doc_1sent'

nlp = Pipeline(_input=path_dataset, pipeline=path_pipeline, _output='file')
annotation = nlp.annotate()