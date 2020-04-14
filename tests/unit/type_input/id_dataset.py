#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

path_pipeline = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/unit/pipeline/custom_pipeline.json'
id_dataset = ''

nlp = Pipeline(_input=id_dataset, pipeline=path_pipeline, _output='file')
annotation = nlp.annotate()