#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

sentence = "I went to the bank to deposit my money."
path_pipeline = '<path_file>/custom_pipeline.yaml'

nlp = Pipeline(_input=sentence, pipeline=path_pipeline, _output='file', boost='ray')

annotation = nlp.annotate()
