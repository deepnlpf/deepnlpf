#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from deepnlpf.pipeline import Pipeline

custom_pipeline_file = ""

custom_pipeline_string = """
{
  "lang": "en",
  "tools": [
    {
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
    },
    {
      "spacy": {
        "pipeline": [
          "pos",
          "tag",
          "shape",
          "is_alpha",
          "is_title",
          "like_num",
          "label"
        ]
      }
    }
  ]
}
"""

id_dataset = "5e74040190fa053af333ceea"

sentences_pt = "Eu amo mais você do que eu!"
sentences = "Barack Obama was born in Hawaii. Hello, how are you. I am doing fine."
sentence = "Barack Obama was born in Hawaii."

nlp = Pipeline(raw_text=sentence, json_string=custom_pipeline_string, boost='ray')
#nlp = Pipeline(raw_text=sentences, json_string=custom_pipeline_string, output_format='xml')

# nlp = Pipeline(raw_text=sentences, json_file=custom_pipeline_file)

#nlp = Pipeline(id_dataset=id_dataset, json_string=custom_pipeline_string)
annotation = nlp.annotate()
print(json.dumps(annotation, indent=4))
