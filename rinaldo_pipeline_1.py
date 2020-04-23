#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

path_dataset_tests = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/data/dataset_2doc_1sent'
sentence = 'Barack Obama was born in Hawaii.'

path_pipeline = '/home/fasr/Mestrado/Workspace/deepnlpf2/rinaldo_pipeline_1.json'
path_dataset = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/data/semeval2010'


nlp = Pipeline(_input=path_dataset, pipeline=path_pipeline, _output='file', _format='xml', 
                boost='ray', memory=17179869184)

annotation = nlp.annotate()

print(annotation)