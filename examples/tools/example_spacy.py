#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deepnlpf.pipeline import Pipeline

# Types of data entries for processing.
sentence = "I went to the bank to deposit my money."

raw_text = "I went to the bank to deposit my money. This is a test sentence for stanza."

path_dataset_1doc_1sent = (
    "/home/fasr/Mestrado/deepnlpf/examples/data/dataset_1doc_1sent"
)
path_dataset_1doc_2sent = (
    "/home/fasr/Mestrado/deepnlpf/examples/data/dataset_1doc_2sent"
)
path_dataset_2doc_1sent = (
    "/home/fasr/Mestrado/deepnlpf/examples/data/dataset_2doc_1sent"
)

id_dataset = ""

path_pipeline = (
    "/home/fasr/Mestrado/deepnlpf/examples/pipelines/json/spacy.json"
)

nlp = Pipeline(_input=sentence, pipeline=path_pipeline, _output="file")
annotation = nlp.annotate()
