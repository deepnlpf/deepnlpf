from deepnlpf.preprocessing import PreProcessing

# /home/fasr/Mestrado/Relation Extraction/Dataset/BB-rel/BioNLP-OST-2019_BB

path_dataset = "/home/fasr/Mestrado/deepnlpf/examples/data/aclImdb"
path_pipeline = "/home/fasr/Mestrado/deepnlpf/examples/pipelines/json/stanza.json"

nlp = PreProcessing(_input=path_dataset, pipeline=path_pipeline, _output='file', use_db="mongodb")
nlp.processing()