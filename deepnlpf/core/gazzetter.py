#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Class: MyGate
    Description:
    Data: 20/09/2018
"""

import os

from deepnlpf.conn.mongodb import ConnectMongoDB
from requests.structures import CaseInsensitiveDict


# import config.settings as config


class MyGate(object):
    '''
        Interface Access Category Gazetteer Gate
    '''

    gazzetter_dict = CaseInsensitiveDict({})

    def __init__(self):
        self.db = ConnectMongoDB()
        # self.load_files(config.PATH['path_dir_gate'])
        self.save('/home/fasr/Mestrado/Workspace/dash-cnlp/resources/dict/gazetteer-gate-8.5.1/')

    def save(self, _path):
        """
        """
        for file in os.listdir(_path):
            if file.endswith('.lst'):
                category = file.split('.')
                #print("category: ", category[0])
                f = open(_path + file, 'rb')
                data = f.read().decode('utf8', 'ignore')
                item = []
                for line in data.split('\n'):
                    if line != '':
                        item.append(line)

                self.db.insert_document('gazzetter', {category[0]:item})

    def load_files(self, _path):
        """
        """
        for file in os.listdir(_path):
            if file.endswith('.lst'):
                category = file.split('.')
                line = open(_path + file).read()
                for word in line.split('\n'):
                    if word != '':
                        self.gazzetter_dict.setdefault(word, []).append(category[0])

    def format_set(self, _data):
        '''
        '''
        return ', '.join([s for s in set(_data)])

    def get_category(self, _token):
        """
            _token: input word.
            return: output category is word.
        """
        if self.gazzetter_dict.get(_token):
            return self.format_set(set(self.gazzetter_dict.get(_token)))
        else:
            return 'null'

if __name__ == "__main__":
    g = MyGate()