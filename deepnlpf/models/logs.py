# -*- coding: utf-8 -*-

class Logs(object):

    def __init__(self):
        from deepnlpf.helpers.mongodb import ConnectMongoDB
        self.db = ConnectMongoDB()

    def save(self, document):
        db_response = self.db.insert_document('logs', document)
        return db_response

    def select(self, key):
        db_response = self.db.select_document('logs', key)
        if db_response:
            return db_response
        else:
            return db_response

    def select_all(self):
        db_response = self.db.select_document_all('logs')
        if db_response:
            return db_response
        else:
            return db_response

    def update(self, key, document):
        db_response = self.db.update('logs', key, document)
        if db_response:
            return "Corpus Successfully Updated!"
        else:
            return "Corpus Update Error!"

    def delete(self, key):
        _key = {"_id": ObjectId(key)}
        db_response = self.db.delete('logs', _key)
        if db_response.deleted_count == 1:
            return {'logs': {'delete': True}}
        else:
            return {'logs': {'delete': False}}
