#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta

class IPluginDB(object, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        raise NotImplementedError('subclasses must override __init__(self) !')

    @abstractmethod
    def insert(self, collection, document):
        raise NotImplementedError('subclasses must override insert(self, collection, document)')

    @abstractmethod
    def select_one(self, collection, key):
        raise NotImplementedError('subclasses must override select_one(self, collection, key)')

    @abstractmethod
    def select_all(self, collection):
        raise NotImplementedError('subclasses must override out_format() !')

    @abstractmethod
    def select_all_key(self, collection, key):
        raise NotImplementedError('subclasses must override select_all_key(self, collection, key)')

    @abstractmethod
    def update(self, collection, key, document):
        raise NotImplementedError('subclasses must override update(self, collection, key, document)')

    @abstractmethod
    def delete(self, collection, key):
        raise NotImplementedError('subclasses must override delete(self, collection, key)')