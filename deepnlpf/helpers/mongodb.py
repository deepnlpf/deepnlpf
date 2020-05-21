#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Path: deepnlpf/conn/
    File: mongodb.py
    Class: ConnectMongoDB
    Description:
    Date: 23/03/2019
"""
from mongoengine import *
from pymongo import MongoClient

from deepnlpf.config import database


class ConnectMongoDB(object):

    def __init__(self):
        self.client = MongoClient(database.DB['hostname'], database.DB['port'], maxPoolSize=200)
        #self.client.authenticate(database.DB['username'], database.DB['password'])
        self.db = self.client[database.DB['database']]
        self.conn()

    def conn(self):
        return self.db

    def insert_document(self, collection_name, document):
        """
            @param collection_name

            @param document

            @return document_id
        """
        try:
            collection = self.db[collection_name]
            _id = collection.insert_one(document).inserted_id
            return _id
        except Exception as err:
            return err

    def select_document(self, collection_name, key):
        """
            @param collection_name

            @param key
        """
        try:
            collection = self.db[collection_name]
            result = collection.find_one(key)
            if(result):
                return result
            else:
                return False
        except Exception as err:
            return err

    def select_document_all_key(self, collection_name, key):
        """
            @param collection_name

            @param key
        """
        try:
            collection = self.db[collection_name]
            result = collection.find(key)
            
            annotations = []
            
            for anotation in result:
                annotations.append(anotation)

            return annotations
        except Exception as err:
            return err

    def select_document_all(self, collection_name):
        try:
            collection = self.db[collection_name]
            item = []

            for data in collection.find():
                item.append(data)

            return item
        except Exception as err:
            return err

    def update(self, collection_name, key, document):
        """
            @param collection_name

            @param key

            @param document
        """
        try:
            collection = self.db[collection_name]
            result = collection.update_one(key, document)
            return result
        except Exception as err:
            return err

    def delete(self, collection_name, key):
        """
            @param key

            @param document
        """
        try:
            collection = self.db[collection_name]
            result = collection.delete_one(key)
            return result
        except Exception as err:
            return err
