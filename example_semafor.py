#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

# Types of data entries for processing.
sentence = "I went to the bank to deposit my money."

raw_text = "I went to the bank to deposit my money. This is a test sentence for semafor."

path_dataset_1doc_1sent = ""
path_dataset_1doc_2sent = ""
path_dataset_2doc_1sent = ""

id_dataset = ""

path_pipeline = "/home/fasr/Mestrado/deepnlpf/examples/pipelines/json/semafor.json"

nlp = Pipeline(_input=sentence, pipeline=path_pipeline, _output='file')
annotation = nlp.annotate()
