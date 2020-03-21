#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deepnlpf.pipeline import Pipeline

json_file = "/home/fasr/Mestrado/Workspace/deepnlpf2/examples/custom_pipeline/stanfordcorenlp.json"

json_string = """
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

nlp = Pipeline(json_file=json_file)
nlp.annotate()