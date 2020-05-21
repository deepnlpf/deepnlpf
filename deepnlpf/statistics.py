# -*- coding: utf-8 -*-

import random
from collections import Counter

import nltk
import plotly
import plotly.graph_objects as go
from bson.objectid import ObjectId
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from plotly.offline import plot

from deepnlpf.models.statistics import Statistics as s
from deepnlpf.modules.utils.preprocessing import PreProcessing


class Statistics(object):
    """
        Generates basic statistics of the corpus.
    """

    word_list = []
    list_sentences = []

    stopWords = set(stopwords.words('english'))

    def __init__(self, id_corpus):
        self._id_dataset = id_corpus
        self._corpus = Dataset().select({"_id": ObjectId(id_corpus)})
        self._documents = Document().select_one({"_id_dataset": ObjectId(id_corpus)})

        self.word_list = self.generate_wordlist()
        self.list_sentences = self.generate_sentencelist()

    def generate_wordlist(self, ):
        """[summary]
            Gera uma lista palavras.

        Returns:
            [type] -- [description]
        """
        print(self._documents['sentences'])
        for sentence in self._documents['sentences']:
            words = PreProcessing().remove_special_characters(sentence).split()

            for word in words:
                self.word_list.append(word.lower())

        return self.word_list

    def generate_sentencelist(self):
        """[Gera uma lista de sentenças.]

        Returns:
            [type] -- [description]
        """
        for sentence in self._documents['sentences']:
            self.list_sentences.append(
                PreProcessing().remove_special_characters(sentence))

        return self.list_sentences

    def min_max_tokens_sentences(self):
        """[Gera uma lista de sentenças tokenizadas.]

        Returns:
            [type] -- [description]
        """
        data_temp = []

        for sentence in self.list_sentences:
            data_temp.append(len(nltk.word_tokenize(sentence)))

        return min(data_temp), max(data_temp)

    def count_tokens(self):
        """[summary]
            Conta o número de tokensna word_list.

        Returns:
            [type] -- [description]
        """
        return len(self.word_list)

    def count_sentences(self):
        """[summary]
            Conta o número de sentenças na lista de sentenças.

        Returns:
            [type] -- [description]
        """
        return len(self._documents['sentences'])

    def frequency_of_words(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        wordlistfreq = []

        for word in self.word_list:
            if word.lower() is not wordlistfreq:
                item = {
                    "word": word.lower(),
                    "freq": self.word_list.count(word)
                }
                wordlistfreq.append(item)

        return wordlistfreq

    def average_sentences(self):
        '''
            Calculates the average size of the phrase by number of tokens.
            Calcula o tamanho médio das frase por número de tokens.

            @return number of tokens.
        '''
        t_tokens = self.count_tokens()
        t_sentences = self.count_sentences()

        # verifica se os divisores são maiores que 0
        if t_tokens > 0 and t_sentences > 0:
            result = t_tokens / t_sentences
            return "%.0f"%result 
        else:
            return 0

    def pos_tag(self):
        '''
            Verifica o POS TAG de cada Token
            @return postaglist
        '''
        # [Alphabetical list of part-of-speech tags used in the Penn Treebank Project:](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)
        postaglist = []

        for word in nltk.pos_tag(self.word_list):
            postaglist.append(word)

        return postaglist

    def freq_pos_tag(self):
        postaglist = []
        listfreq = []

        for item in self.pos_tag():
            postaglist.append(item[1])

        for item in Counter(postaglist).items():
            data = {
                "pos": item[0],
                "freq": item[1]
            }

            listfreq.append(data)

        return listfreq

    def freq_word(self):
        temp_list = []

        for item in Counter(self.word_list).items():
            data = {
                "word": item[0],
                "freq": item[1]
            }

            temp_list.append(data)

        return temp_list

    def cont_tokens_sentence(self, list_sentences):
        """[Calcula o número de tokens por sentença.]

        Returns:
            [list] -- [retorna uma lista contendo o número de palavras por sentenças.]
        """
        data = []

        for sentence in list_sentences:
            data.append(len(word_tokenize(sentence)))

        return data

    def full_statistics(self, save=False):
        """
            This function returns to the user a complete statistic of the corpus.

            This param paramser when true saves the statistics in the database.
            @param save=False

            @return full statistics data json.
        """

        _min, _max = self.min_max_tokens_sentences()

        document = {
            "_id_dataset": self._id_dataset,
            "total_sentences": self.count_sentences(),
            "total_tokens": self.count_tokens(),
            "num_min_tokens_sentences": _min,
            "num_max_tokens_sentences": _max,
            "average_tokens_sentences": self.average_sentences(),
            "words_frequency": self.frequency_of_words(),
            "tokens_frequency_to_sentences": self.cont_tokens_sentence(self.list_sentences),
            "post_tag_frequency": self.freq_pos_tag()
        }

        if save is True:
            return self.save_statistics(document)
        else:
            return document

    def split_pos_tag(self, _corpus, _lemma=False):
        '''
            Calculates the frequency number of tokens per class, in different lists.
            Calcula o número de frequência de tokens por classes, em listas diferentes.
            @param
                _corpus
                _lemma
            @return
        '''
        data_temp = []

        for line in _corpus:

            if _lemma is False:
                words_tokens = word_tokenize(line)
            else:
                words_tokens = []
                lemmatizer = WordNetLemmatizer()

                for word in word_tokenize(line):
                    if word.isalpha():
                        words_tokens.append(lemmatizer.lemmatize(word))

            for word in nltk.pos_tag(words_tokens):
                if word[0].isalpha():
                    data_temp.append(word[1])

        return data_temp

    def hist_token_frequency_by_class_grammtical(self):
        #'Dataset {}'.format(self._id_dataset),
        # ['Adverb', 'Adjective', 'Verb', 'Noun']

        fig = go.Figure()

        for item in Counter(self.split_pos_tag(self.list_sentences)).items():
            cont = []

            for _ in range(int(item[1])):
                cont.append(item[0])

            fig.add_trace(go.Histogram(x=cont, name=item[0]))

        fig.update_layout(
            title_text='Frequency of Tokens to Grammatical Class',
            xaxis_title_text='Grammatical Class',
            yaxis_title_text='Words Frequency',
            bargap=0.2,
            bargroupgap=0.1,
            showlegend=True
        )

        fig.show()

    def hist_token_frequency_by_sentences(self, _title_text='Number Tokens for Sentences', _xaxis_title_text='Number Tokens.', _yaxis_title_text='Sentences Frequency'):
        """[Histogram - frequency of tokens by sentences.]

        Keyword Arguments:
            _title_text {str} -- [description] (default: {'Number Tokens for Sentences'})
            _xaxis_title_text {str} -- [description] (default: {'Number Tokens.'})
            _yaxis_title_text {str} -- [description] (default: {'Sentences Frequency'})
        """
        fig = go.Figure(
            data=[go.Histogram(
                x=self.cont_tokens_sentence(self.list_sentences))]
        )

        fig.update_layout(
            title_text=_title_text,
            xaxis_title_text=_xaxis_title_text,
            yaxis_title_text=_yaxis_title_text,
            bargap=0.2,
            bargroupgap=0.1
        )

        fig.show()

    def word_cloud(self, quant_word=50):
        """[summary]
        
        Keyword Arguments:
            quant_word {int} -- [description] (default: {50})
        """
        wordsFiltered = []

        for word in self.word_list:
            if word not in self.stopWords:
                wordsFiltered.append(word)

        words = wordsFiltered[:quant_word]
        
        colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(
            1, 10)] for i in range(quant_word)]

        weights = [random.randint(15, 35) for i in range(quant_word)]

        data = go.Scatter(x=[random.random() for i in range(quant_word)],
                          y=[random.random() for i in range(quant_word)],
                          mode='text',
                          text=words,
                          marker={'opacity': 0.3},
                          textfont={'size': weights,
                                    'color': colors})

        layout = go.Layout({'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                            'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}})

        fig = go.Figure(data=[data], layout=layout)

        plot(fig)

    def save_statistics(self, document):

        req = self.check_statistics_exist()

        if(req):
            return req
        else:
            return s().save(document)

    def check_statistics_exist(self):
        key = {"_id_dataset": self._id_dataset}
        return s().select(key)
