#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from deepnlpf.pipeline import Pipeline


custom_pipeline_string = """
{
    "lang": "en",
    "tools": [
        {
            "supwsd": {
                "pipeline": [
                    "wsd"
                ]
            }
        }
    ]
}
"""

sentence = "The human brain is quite proficient at word-sense disambiguation."

def main():
  nlp = Pipeline(raw_text=sentence, json_string=custom_pipeline_string)
  annotation = nlp.annotate()
  print(json.dumps(annotation))

if __name__ == "__main__":
    main()