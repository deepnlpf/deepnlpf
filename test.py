#!/usr/bin/python3
# _*_coding:utf-8_*_

from stanfordcorenlp import StanfordCoreNLP

sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'

nlp = StanfordCoreNLP(memory='8g')
print(nlp.annotate(sentence))
nlp.close()