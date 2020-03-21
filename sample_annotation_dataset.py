#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deepnlpf.pipeline import Pipeline

custom_pipeline_file = "/home/fasr/Mestrado/Workspace/deepnlpf2/examples/custom_pipeline/stanfordcorenlp.json"

custom_pipeline_string = """
{
    "tools": [{
        "stanfordcorenlp": {
            "pipeline": [
                "tokenize",
                "ssplit",
                "pos",
                "lemma",
                "ner",
                "parse",
                "depparse",
                "truecase",
                "dcoref"
            ]
        }
    }]
}
"""

id_dataset = "5e74040190fa053af333ceea"

sentence = "Barack Obama was born in Hawaii. Hello, how are you. I am doing fine."

nlp = Pipeline(raw_text=sentence, json_string=custom_pipeline_string)
#nlp = Pipeline(raw_text=sentence, json_string=custom_pipeline_string, output_format='xml')

#nlp = Pipeline(id_dataset=id_dataset, json_string=custom_pipeline_string)
nlp.annotate()