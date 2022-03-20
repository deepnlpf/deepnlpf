from deepnlpf.pipeline import Pipeline

path_pipeline = "/home/fasr/deepnlpf/deepnlpf/pipeline.json"

sentence = "Barack Obama was born in Hawaii."

nlp = Pipeline(_input=sentence, pipeline=path_pipeline, _output="file")
nlp.annotate()