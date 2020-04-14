"""
    Statistics
"""
from deepnlpf.statistics import Statistics

id_corpus_5 = '5d30ad8b6db30e050d584fb3'
id_corpus_1000 = '5d30ad8b6db30e050d584fb5'
id_corpus_4000 = '5d30ad8b6db30e050d584fb7'
id_corpus_8000 = '5d30ad8b6db30e050d584fb9'

statistics = Statistics(id_corpus_8000)

#statistics.full_statistics(save=True)
#statistics.hist_token_frequency_by_sentences()
#statistics.hist_token_frequency_by_class_grammtical()
statistics.word_cloud(20)