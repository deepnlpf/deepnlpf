#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from deepnlpf.pipeline import Pipeline

custom_pipeline_string = """
{
    "lang": "en",
    "tools": [
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

sentence = "I went to the bank to deposit my money."

def main():
  nlp = Pipeline(raw_text=sentence, json_string=custom_pipeline_string, boost='ray')
  annotation = nlp.annotate()
  print(json.dumps(annotation))

if __name__ == "__main__":
    main()