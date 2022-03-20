from deepnlpf.pipeline import Pipeline

path_pipeline = "/home/fasr/deepnlpf/deepnlpf/pipeline.json"

sentence = "The quick brown fox jumped over the lazy dog."

nlp = Pipeline(_input=sentence, pipeline=path_pipeline, _output="file")
nlp.annotate()