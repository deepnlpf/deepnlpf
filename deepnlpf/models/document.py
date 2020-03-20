# -*- coding: utf-8 -*-

from deepnlpf.logs import logs

class Document(object):

    def __init__(self):
        from deepnlpf.helpers.mongodb import ConnectMongoDB
        self.db = ConnectMongoDB()

    def save(self, document):
        try:
            db_response = self.db.insert_document('document', document)
            db_response = {'document': {'_id': db_response}}
            return db_response
        except Exception as err:
            logs.logger.error("🐞 Saved Document  " + str(err))

    def select_one(self, _id_dataset):
        db_response = self.db.select_document('document', _id_dataset)
        if db_response:
            return db_response
        else:
            return db_response

    def select_all(self, _id_dataset):
        db_response = self.db.select_document_all_key('document', _id_dataset)
        if db_response:
            return db_response
        else:
            return db_response

    def update(self, key, document):
        db_response = self.db.update('document', key, document)
        if db_response:
            return "Corpus Successfully Updated!"
        else:
            return "Corpus Update Error!"

    def delete(self, key):
        _key = {"_id": ObjectId(key)}
        db_response = self.db.delete('document', _key)
        if db_response.deleted_count == 1:
            return {'document': {'delete': True}}
        else:
            return {'document': {'delete': False}}
