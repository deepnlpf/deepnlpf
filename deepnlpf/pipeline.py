#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Date: 03/03/2019
"""

import os, sys, json, uuid, names, datetime

from tqdm import tqdm
from bson.objectid import ObjectId

from deepnlpf.config import config

from deepnlpf.models.dataset import Dataset
from deepnlpf.models.document import Document
from deepnlpf.models.analysis import Analysis

from deepnlpf.core.util import Util
from deepnlpf.core.boost import Boost
from deepnlpf.core.encoder import JSONEncoder
from deepnlpf.core.output_format import OutputFormat
from deepnlpf.core.plugin_manager import PluginManager


class Pipeline(object):
    
    def __init__(self, plugin_base='stanza', id_dataset=None, raw_text=None,
                 json_string=None, json_file=None, save_analysis=True, _print='terminal',
                 output_format='json'):

        self.documents = None

        self._plugin_base = plugin_base

        if id_dataset != None and raw_text is None:
            self.id_dataset = id_dataset
            self.type_input_data = True
        elif raw_text != None and id_dataset is None:
            self.raw_text = raw_text
            self.type_input_data = False
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
        self._print = _print
        self._output_format = output_format
        self._id_pool = ObjectId(b'foo-bar-quux')

    def annotate(self):
        # check type input date.
        if self.type_input_data:
            self.documents = Document().select_all(
                {"_id_dataset": ObjectId(self.id_dataset)})
        else:
            # parsing join tokens in sentence.
            sentences = list()

            # load sentences.
            document = json.loads(json.dumps({'sentences': [self.raw_text]}))

            # pre-processing tokenization and ssplit using plugin base selected.
            if self._plugin_base == "stanza":
                self.documents = PluginManager().call_plugin(
                    plugin_name='stanza',
                    _id_pool=self._id_pool, 
                    document=document, 
                    pipeline=['tokenize']
                    )
                
                # loop - go through the json and assemble the sentences.
                for item in self.documents[0]:
                    sentence = list()
                    for data in item:
                        sentence.append(data['text'])
                    sentences.append(" ".join(sentence))

            if self._plugin_base == "stanfordcorenlp":
                self.documents = PluginManager().call_plugin(
                    plugin_name='stanfordcorenlp',
                    _id_pool=self._id_pool, 
                    document=document, 
                    pipeline=['ssplit']
                    )

                # loop - go through the json and assemble the sentences.
                for item in self.documents[0]['sentences']:
                    sentence = list()
                    for token in item['tokens']:
                        sentence.append(token['word'])
                    sentences.append(" ".join(sentence))        

            # save database.
            _id_dataset = Dataset().save({
                "name": names.get_first_name(),
                "data_time": OutputFormat.data_time(self)
            })

            # save documents.
            Document().save({
                "_id_dataset": _id_dataset,
                "name": names.get_first_name(),
                "sentences": [sentence for sentence in sentences]
            })

            # get documents.
            self.documents = Document().select_all(
                {"_id_dataset": ObjectId(_id_dataset)})

        # Runs the tools using multiprocessor parallelism techniques.
        # get tools names
        self.list_tools = [','.join(tool.keys()) for tool in self._custom_pipeline['tools']]

        # set index number in tools.
        new_list_tools = [str(tool)+'-'+str(index) for index, tool in enumerate(self.list_tools)]

        return Boost().parallelpool(self.run, new_list_tools)

    def run(self, _tool_name):
        """
            Description: Here you will execute a process for each tool. 
                         In this function, you must integrate your new tool into the pipeline
                         if you have added a new plugin, see documentation in case of doubts.

            @param _tool_name
        """
        # extraction index number in tools, get args.
        plugin_name, index = _tool_name.split('-')

        for document in tqdm(self.documents):
            pipeline = self._custom_pipeline['tools'][int(
                index)][plugin_name]['pipeline']

            annotation = PluginManager().call_plugin(
                plugin_name=plugin_name,
                _id_pool=self._id_pool, 
                document=document, 
                pipeline=pipeline
                )

            self.save_analysis(plugin_name, annotation)

            remove_object_id = JSONEncoder().encode(annotation)
            data_json = json.loads(remove_object_id)
            data_formating = self.output_format(data_json)
            return self.output(data_formating)

    def save_analysis(self, tool, annotation):
        if self._save_annotation:
            Analysis().save(annotation)
        else:
            return annotation

    def output_format(self, annotation):
        if self._output_format == "xml":
            return OutputFormat().json2xml(annotation)
        return annotation

    def output(self, annotation):
        if self._print == 'terminal':
            return annotation
        elif self._print == 'browser':
            from flask import Flask, escape, request
            app = Flask(__name__)

            @app.route('/')
            def hello():
                name = request.args.get("name", annotation)
                return f'Hello, {escape(name)}!'

            app.run(debug=True)
