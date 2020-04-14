#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from deepnlpf.pipeline import Pipeline


custom_pipeline_string = """
  {
    "lang": "en",
    "tools": [
      { "pywsd": { "pipeline": ["wsd"] } }
    ]
  }
    """

sentence = "I went to the bank to deposit my money."

def main():
  nlp = Pipeline(raw_text=sentence, json_string=custom_pipeline_string)
  annotation = nlp.annotate()
  print(json.dumps(annotation))

if __name__ == "__main__":
    main()