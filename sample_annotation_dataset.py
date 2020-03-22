#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deepnlpf.pipeline import Pipeline

custom_pipeline_file = ""

custom_pipeline_string = """
{
    "lang": "en",
    "threads": 4,
    "tools": [
        {
            "semafor": {
                "pipeline": [
                    "parsing"
                ]
            }
        }
    ]
}
"""

id_dataset = "5e74040190fa053af333ceea"

sentences = "Barack Obama was born in Hawaii. Hello, how are you. I am doing fine."

nlp = Pipeline(raw_text=sentences, json_string=custom_pipeline_string)
#nlp = Pipeline(raw_text=sentences, json_string=custom_pipeline_string, output_format='xml')

# nlp = Pipeline(raw_text=sentences, json_file=custom_pipeline_file)

#nlp = Pipeline(id_dataset=id_dataset, json_string=custom_pipeline_string)
nlp.annotate()