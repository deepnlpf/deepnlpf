#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from deepnlpf.pipeline import Pipeline

sentence = "The human brain is quite proficient at word-sense disambiguation."
path_pipeline = "/home/fasr/Mestrado/deepnlpf/tests/pipelines/json/stanfordcorenlp.json"

nlp = Pipeline(_input=sentence, pipeline=path_pipeline, _output='file')
annotation = nlp.annotate()