#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

# Types of data entries for processing.
sentence = "I went to the bank to deposit my money."

raw_text = "The boy gave the frog to the girl. The boy's gift was to the girl. The girl was given a frog."

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

path_pipeline = "/home/fasr/Mestrado/deepnlpf/examples/pipelines/json/stanza.json"

nlp = Pipeline(
    _input=sentence, pipeline=path_pipeline, _output="file", use_db="mongodb"
)

results = nlp.annotate()
