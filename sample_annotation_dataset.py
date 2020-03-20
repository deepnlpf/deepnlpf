#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.core.util import Util
from deepnlpf.pipeline import Pipeline

path_custom_pipeline = "/home/fasr/Mestrado/Workspace/deepnlpf2/examples/custom_pipeline/stanfordcorenlp.json"
id_dataset = "5e74040190fa053af333ceea"

custom_pipeline = Util().openfile_json(path_custom_pipeline)

nlp = Pipeline(id_dataset, custom_pipeline, True)
nlp.annotate()