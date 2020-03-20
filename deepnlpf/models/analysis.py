# -*- coding: utf-8 -*-
from deepnlpf.logs import logs

class Analysis(object):

    def __init__(self):
        from deepnlpf.helpers.mongodb import ConnectMongoDB
        self.db = ConnectMongoDB()

    def save(self, document):
        try:
            db_response = self.db.insert_document('analysis', document)
            db_response = {'analysis': {'_id': db_response}}
            return db_response
        except Exception as err:
            logs.logger.error("🐞 Saved analysis  " + str(err))

    def select_one(self, _id_dataset):
        db_response = self.db.select_document('analysis', _id_dataset)
        if db_response:
            return db_response
        else:
            return db_response

    def select_all(self, _id_dataset):
        db_response = self.db.select_document_all_key('analysis', _id_dataset)
        if db_response:
            return db_response
        else:
            return db_response

    def update(self, key, document):
        db_response = self.db.update('analysis', key, document)
        if db_response:
            return "analysis Successfully Updated!"
        else:
            return "analysis Update Error!"

    def delete(self, key):
        _key = {"_id": ObjectId(key)}
        db_response = self.db.delete('analysis', _key)
        if db_response.deleted_count == 1:
            return {'document': {'delete': True}}
        else:
            return {'document': {'delete': False}}
