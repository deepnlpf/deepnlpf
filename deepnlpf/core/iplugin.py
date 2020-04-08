#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta

class IPlugin(object, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, id_pool, lang, document, pipeline, **args):
        raise NotImplementedError('subclasses must override __init__() !')

    @abstractmethod
    def run(self):
        raise NotImplementedError('subclasses must override run() !')

    @abstractmethod
    def wrapper(self):
        raise NotImplementedError('subclasses must override wrapper() !')

    @abstractmethod
    def out_format(self, annotation):
        raise NotImplementedError('subclasses must override out_format() !')
