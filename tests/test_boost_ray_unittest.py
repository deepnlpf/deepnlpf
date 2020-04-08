#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import json

from deepnlpf.pipeline import Pipeline

class TestBoostRayUnittest(unittest.TestCase):

  def __init__(self):
    self.custom_pipeline_string = """
    {
      "lang": "en",
      "tools": [
        { "stanza": { "pipeline": ["tokenize", "mwt", "pos", "lemma", "ner", "depparse" ] } }
      ]
    }
      """

    self.sentence = "Barack Obama was born in Hawaii."
    self.sentences = "Barack Obama was born in Hawaii. Hello, how are you. I am doing fine."

    self.result = '[{"_id_pool":"666f6f2d6261722d71757578","_id_dataset":"5e8e3a573eb72ef2dd6e596b","_id_document":"5e8e3a573eb72ef2dd6e596d","tool":"stanza","annotation":[[[{"id":"1","text":"Barack","lemma":"Barack","upos":"PROPN","xpos":"NNP","feats":"Number=Sing","head":4,"deprel":"nsubj:pass","misc":"start_char=0|end_char=6"},{"id":"2","text":"Obama","lemma":"Obama","upos":"PROPN","xpos":"NNP","feats":"Number=Sing","head":1,"deprel":"flat","misc":"start_char=7|end_char=12"},{"id":"3","text":"was","lemma":"be","upos":"AUX","xpos":"VBD","feats":"Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin","head":4,"deprel":"aux:pass","misc":"start_char=13|end_char=16"},{"id":"4","text":"born","lemma":"bear","upos":"VERB","xpos":"VBN","feats":"Tense=Past|VerbForm=Part|Voice=Pass","head":0,"deprel":"root","misc":"start_char=17|end_char=21"},{"id":"5","text":"in","lemma":"in","upos":"ADP","xpos":"IN","head":6,"deprel":"case","misc":"start_char=22|end_char=24"},{"id":"6","text":"Hawaii","lemma":"Hawaii","upos":"PROPN","xpos":"NNP","feats":"Number=Sing","head":4,"deprel":"obl","misc":"start_char=25|end_char=31"},{"id":"7","text":".","lemma":".","upos":"PUNCT","xpos":".","head":4,"deprel":"punct","misc":"start_char=32|end_char=33"}]]],"data_time":"\"08/04/2020 - 17:55:55\"","_id":"5e8e3a5bdd290217dd1bde43"}]'

  def main(self):
    nlp = Pipeline(raw_text=sentences, json_string=custom_pipeline_string, boost='ray')
    
    annotation = nlp.annotate()
    result = json.dumps(annotation)
    print(result)
    
    # self.assertEqual(annotation, result, "Err!")

if __name__ == "__main__":
    unittest.main()