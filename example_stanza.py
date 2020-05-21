#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

# Types of data entries for processing.
sentence = "I went to the bank to deposit my money."

raw_text = "I went to the bank to deposit my money. This is a test sentence for stanza."

path_dataset_1doc_1sent = "/home/fasr/Mestrado/deepnlpf/examples/data/dataset_1doc_1sent"
path_dataset_1doc_2sent = "/home/fasr/Mestrado/deepnlpf/examples/data/dataset_1doc_2sent"
path_dataset_2doc_1sent = "/home/fasr/Mestrado/deepnlpf/examples/data/dataset_2doc_1sent"

id_dataset = ""

path_pipeline = "/home/fasr/Mestrado/deepnlpf/examples/pipelines/json/stanza.json"

pipeline_json_string = """
{
    "lang": "en",
    "tools": {
        "stanza": {
            "processors": [
                "tokenize",
                "mwt",
                "pos",
                "lemma",
                "ner",
                "depparse"
            ]
        }
    }
}
"""

pipeline_json_url = "https://raw.githubusercontent.com/deepnlpf/deepnlpf/master/examples/pipelines/json/stanza.json"
pipeline_yaml_url = "https://raw.githubusercontent.com/deepnlpf/deepnlpf/master/examples/pipelines/yaml/stanza.yaml"


nlp = Pipeline(
    _input=sentence,
    pipeline=pipeline_json_url,
    _output="file"
)

results = nlp.annotate()
