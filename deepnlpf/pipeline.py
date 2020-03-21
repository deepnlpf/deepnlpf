#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Date: 03/03/2019
"""


import os, sys, json, uuid

from tqdm import tqdm
from bson.objectid import ObjectId

from deepnlpf.config import config
from deepnlpf.core.boost import Boost
from deepnlpf.models.document import Document
from deepnlpf.models.analysis import Analysis
from deepnlpf.core.plugin_manager import PluginManager

class Pipeline(object):
    """
        Description: Pipeline class is ..
    """

    plugin = []

    def __init__(self, id_dataset, custom_pipeline, save_analysis=False):
        self.id_dataset = id_dataset
        self._custom_pipeline = custom_pipeline
        self._save_annotation = save_analysis
        self._id_pool = ObjectId(b'foo-bar-quux')

    def annotate(self):
        """
            Description: The main method for initiating the process of 
                         the linguisticas tools and analyzes to be executed.
        """
        # Runs the tools using multiprocessor parallelism techniques.

        # get tools names
        self.list_tools = [','.join(tool.keys()) for tool in self._custom_pipeline['tools']]

        # set index number in tools.
        new_list_tools = [str(tool)+'-'+str(index) for index, tool in enumerate(self.list_tools)]

        result = Boost().parallelpool(self.run, new_list_tools)

        return result

    def run(self, _tool_name):
        """
            Description: Here you will execute a process for each tool. 
                         In this function, you must integrate your new tool into the pipeline
                         if you have added a new plugin, see documentation in case of doubts.

            @param _tool_name
        """
        # extraction index number in tools, get args.
        plugin_name, index = _tool_name.split('-')

        documents = Document().select_all({"_id_dataset": ObjectId(self.id_dataset)})

        for document in tqdm(documents):
            pipeline = self._custom_pipeline['tools'][int(index)][plugin_name]['pipeline']

            annotation = PluginManager().call_plugin(plugin_name=plugin_name, 
                _id_pool=self._id_pool, document=document, pipeline=pipeline)

            self.save_analysis(plugin_name, annotation)

    def save_analysis(self, tool, annotation):
        if self._save_annotation  is True:
            if(Analysis().save(annotation)):
                return annotation
        else:
            return annotation