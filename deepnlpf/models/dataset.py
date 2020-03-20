# -*- coding: utf-8 -*-

from bson.objectid import ObjectId

class Dataset(object):

    def __init__(self):
        from deepnlpf.helpers.mongodb import ConnectMongoDB
        self.db = ConnectMongoDB()

    def save(self, document):
        db_response = self.db.insert_document('dataset', document)
        return db_response

    def select(self, key):
        db_response = self.db.select_document('dataset', key)
        if db_response:
            return db_response
        else:
            return db_response

    def select_all(self):
        db_response = self.db.select_document_all('dataset')
        if db_response:
            return db_response
        else:
            return db_response

    def update(self, key, document):
        db_response = self.db.update('dataset', key, document)
        if db_response:
            return "Dataset Successfully Updated!"
        else:
            return "Dataser Update Error!"

    def delete(self, id_dataset):
        id_dataset = {"_id": ObjectId(id_dataset)}
        db_response = self.db.delete('dataset', id_dataset)

        if db_response.deleted_count:
            return True
        else:
            return False
