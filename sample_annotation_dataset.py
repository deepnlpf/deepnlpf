#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from deepnlpf.pipeline import Pipeline

custom_pipeline_file = ""

custom_pipeline_string = """
{
    "tools": [{
        "stanza": {
            "pipeline": [
                "tokenize",
                "mwt",
                "pos",
                "lemma",
                "ner",
                "depparse"
            ]
        }
    }]
}
"""

id_dataset = "5e74040190fa053af333ceea"

sentences = "Barack Obama was born in Hawaii. Hello, how are you. I am doing fine."

nlp = Pipeline(raw_text=sentences, json_string=custom_pipeline_string)
#nlp = Pipeline(raw_text=sentences, json_string=custom_pipeline_string, output_format='xml')

# nlp = Pipeline(raw_text=sentences, json_file=custom_pipeline_file)

#nlp = Pipeline(id_dataset=id_dataset, json_string=custom_pipeline_string)
annotation = nlp.annotate()
print(json.dumps(annotation, indent=4))