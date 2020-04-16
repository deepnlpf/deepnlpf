#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

path_pipeline = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/data/custom_pipeline.json'
path_dataset = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/data/dataset_1doc_1sent'

sentences = 'Barack Obama was born in Hawaii.'

nlp = Pipeline(_input=sentences, pipeline=path_pipeline, format='xml')
annotation = nlp.annotate()