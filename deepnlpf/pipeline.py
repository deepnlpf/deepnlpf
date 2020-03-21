#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Date: 03/03/2019
"""

import os, sys, json, uuid

from tqdm import tqdm
from bson.objectid import ObjectId

from deepnlpf.config import config

from deepnlpf.models.document import Document
from deepnlpf.models.analysis import Analysis

from deepnlpf.core.util import Util
from deepnlpf.core.boost import Boost
from deepnlpf.core.plugin_manager import PluginManager

class Pipeline(object):
    """
        Description: Pipeline class is ..
    """

    self.type_input_data = NULL
    
    def __init__(self, id_dataset=None, raw_text=None, json_string=None, json_file=None, save_analysis=True):
        
        if id_dataset != None and raw_text is None:
            self.id_dataset = id_dataset
            self.type_input_data = "dataset"
        elif raw_text != None and id_dataset is None:
            self.raw_text = raw_text
            self.type_input_data = "raw_text"
        elif id_dataset != None and raw_text != None:
            print("You cannot enter two data entry parameters.")
            sys.exit(0) 
        else:
            print("Enter an ID of some dataset or some text to be processed!")
            sys.exit(0)

        if json_string != None and json_file is None:
            self._custom_pipeline = json.loads(json_string)
        elif json_file != None and json_string is None:
            self._custom_pipeline = Util().openfile_json(json_file)
        elif json_file != None and json_string != None:
            print("You cannot enter parameters for simultaneous pipelines, choose one!")
            sys.exit(0)
        else:
            print("Enter a parameter from a valid pipeline.")
            sys.exit(0)

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

        if self.type_input_data == "dataset":
            # load documents.
            documents = Document().select_all({"_id_dataset": ObjectId(self.id_dataset)})
        else:
            # ssplit
            pass

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