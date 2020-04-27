#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

#sentence = "Barack Obama was born in Hawaii."
#sentences = "Barack Obama was born in Hawaii. Hello, how are you. I am doing fine."

path_dataset = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/data/dataset_1doc_1sent'
path_pipeline = '/home/fasr/Mestrado/Workspace/deepnlpf2/tests/pipelines/json/stanza.json'

nlp = Pipeline(_input=path_dataset, pipeline=path_pipeline, _output='file', boost='pathos')
annotation = nlp.annotate()