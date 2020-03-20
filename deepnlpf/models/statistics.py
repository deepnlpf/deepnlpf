# -*- coding: utf-8 -*-

"""
    Statistics
"""
class Statistics(object):

    def __init__(self):
        from deepnlpf.helpers.mongodb import ConnectMongoDB
        self.db = ConnectMongoDB()

    def save(self, document):
        db_response = self.db.insert_document('statistics', document)
        db_response = {'statistics': {'_id': db_response}}
        return db_response

    def select(self, key):
        return self.db.select_document('statistics', key)