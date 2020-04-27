#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.pipeline import Pipeline

path_dataset = '<path_dir_dataset>'
path_pipeline = '<path/pipeline.json>'

nlp = Pipeline(_input=path_dataset, pipeline=path_pipeline, _output='file', boost='ray')
annotation = nlp.annotate()

# The output result must be generated at: home / your_name / deepnlpf_date / output