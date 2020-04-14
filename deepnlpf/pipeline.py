#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, json, uuid, names, datetime

from tqdm import tqdm
from bson.objectid import ObjectId

from deepnlpf.models.dataset import Dataset
from deepnlpf.models.document import Document
from deepnlpf.models.analysis import Analysis

from deepnlpf.core.util import Util
from deepnlpf.core.boost import Boost
from deepnlpf.core.encoder import JSONEncoder
from deepnlpf.core.output_format import OutputFormat
from deepnlpf.core.plugin_manager import PluginManager

class Pipeline(object):
    
    def __init__(self, _input=None, pipeline=None, _output=None, _format=None,
        using_db=True, plugin_base=None, boost=None):

        # auto select type input data.
        if _input != None:
            if os.path.isdir(_input):
                self.type_input_data = 'path_dataset'
            elif type(_input) ==  ObjectId:
                self.type_input_data = 'id_dataset'
            elif type(_input) == str:
                self.type_input_data = 'raw_text'
            
            self._input = _input
        else:
            print("Enter a parameter from a valid dataset <path_dataset> or <id_dataset> or <raw_text> !")
            sys.exit(0)

        if pipeline != None:
            # True = Path file , False = String json.
            self._custom_pipeline = Util().openfile_json(pipeline) if os.path.isfile(pipeline) else json.loads(pipeline)
        else:
            print("Enter a parameter from a valid pipeline.")
            sys.exit(0)

        self._using_db = using_db
        self._output = _output
        self._format = _format
        
        self._plugin_base = plugin_base
        self._boost = boost

        self._id_pool = ObjectId(b'foo-bar-quux')

    def annotate(self):
        # Runs the tools using multiprocessor parallelism techniques.
        # get tools names
        self.list_tools = [','.join(tool.keys()) for tool in self._custom_pipeline['tools']]

        # set index number in tools.
        new_list_tools = [str(tool)+'-'+str(index) for index, tool in enumerate(self.list_tools)]

        # If True boost = pathos Else boost = ray
        return Boost().multiprocessing(self.run, new_list_tools) if self._boost is None else Boost().parallel(self.run, new_list_tools)

    def run(self, _tool_name):
        """
            Description: Here you will execute a process for each tool. 
                         In this function, you must integrate your new tool into the pipeline
                         if you have added a new plugin, see documentation in case of doubts.

            @param _tool_name
        """
        # extraction index number in tools, get args.
        plugin_name, index = _tool_name.split('-')

        # get _id_dataset
        _id_dataset = self.option_input_text_selected(self.type_input_data)

        # get documents.
        self.documents = Document().select_all({"_id_dataset": ObjectId(_id_dataset)})

        for document in tqdm(self.documents, desc='Processing document(s)'):
            annotation = PluginManager().call_plugin(
                plugin_name=plugin_name, _id_pool=self._id_pool, 
                lang=self._custom_pipeline['lang'], document=document, 
                pipeline=self._custom_pipeline['tools'][int(index)][plugin_name]['pipeline']
                )

            self.save_analysis(plugin_name, annotation)

            remove_object_id = JSONEncoder().encode(annotation)
            data_json = json.loads(remove_object_id)
            data_formating = self.output_format(data_json)
            return self.output(data_formating, _id_dataset)

    def save_analysis(self, tool, annotation):
        if self._using_db:
            Analysis().save(annotation)
        else:
            return annotation

    def output_format(self, annotation):
        if self._format == "xml":
            return OutputFormat().json2xml(annotation)
        return annotation

    def output(self, annotation, _id_dataset):
        if self._output is None: # terminal
            return annotation
        elif self._output == 'file':
            EXT = '.xml' if self._format else '.json'
            PATH = os.environ['HOME'] + '/deepnlpf_data/output/'+str(_id_dataset)+EXT
            return Util().save_file(PATH, str(annotation))
        elif self._output == 'browser':
            from flask import Flask, escape, request
            app = Flask(__name__)

            @app.route('/')
            def hello():
                name = request.args.get("name", annotation)
                return f'Hello, {escape(name)}!'

            app.run(debug=True)

    def option_input_text_selected(self, type_input_data):
        # check type input data selected.
        if type_input_data == 'id_dataset':
            return self._input
        elif type_input_data == 'raw_text':
            document = json.loads(json.dumps({'sentences': [self._input]}))
            return self.ssplit(document)
        elif type_input_data == 'path_dataset':          
            return self.processing_path_dataset(self._input)

    def ssplit(self, document):
        sentences = list()
        
        # pre-processing tokenization and ssplit using plugin base selected.
        if self._plugin_base is None: #stanza
            self.documents = PluginManager().call_plugin(
                plugin_name='stanza', _id_pool=self._id_pool, 
                lang=self._custom_pipeline['lang'],
                document=document, pipeline=['tokenize'])
            
            # loop - go through the json and assemble the sentences.
            for item in self.documents[0]:
                sentence = list()
                for data in item:
                    sentence.append(data['text'])
                sentences.append(" ".join(sentence))

        if self._plugin_base == "stanfordcorenlp":
            self.documents = PluginManager().call_plugin(
                plugin_name='stanfordcorenlp', _id_pool=self._id_pool,
                lang=self._custom_pipeline['lang'], 
                document=document, pipeline=['ssplit'])

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

        return _id_dataset

    def processing_path_dataset(self, path_dataset, ssplit=False):
        """
            Get the path of the informed dataset, go through the entire directory tree, 
            checking the files to be saved in the database.
        """
        dataset_name = ''

        # check is path dir validate.
        if(os.path.isdir(path_dataset)):

            # check if folder empty.
            if os.listdir(path_dataset) == []:
                print('Folder empty!')
            else:
                # get name corpus
                dataset_name = os.path.basename(os.path.normpath(path_dataset))
                    
                # save corpus
                _id_dataset = Dataset().save({
                    "name": dataset_name,
                    "data_time": datetime.datetime.now()
                })

                # get all files' and folders' names in the current directory.
                dirContents = os.listdir(path_dataset)

                files = []
                subfolders = [] # train or test.

                for filename in dirContents:
                    # check whether the current object is a folder or not.
                    if os.path.isdir(os.path.join(os.path.abspath(path_dataset), filename)):
                        subfolders.append(filename)
                    elif os.path.isfile(os.path.join(os.path.abspath(path_dataset), filename)):
                        files.append(filename)

                if subfolders: # check exist folders
                    data = []

                    for folders_type in subfolders:
                        print("├── {}:".format(folders_type))

                        folders_labels = os.listdir(path_dataset+"/"+folders_type)

                        for _label in folders_labels:
                            cont_doc = 0

                            if os.path.isdir(os.path.join(os.path.abspath(path_dataset+"/"+folders_type), _label)):

                                for file_name in tqdm(os.listdir(path_dataset+"/"+folders_type+"/"+_label+"/"), desc="│   └── documents [{}]".format(_label)):
                                    cont_doc += 1

                                    text_raw = Util().open_txt(path_dataset+"/"+folders_type+"/"+_label+"/"+file_name)
                                    
                                    # Sentence Split.
                                    #sentences = PreProcessing('ssplit', text_raw).run()

                                    item = {
                                        "_id_dataset": _id_dataset,
                                        "name": file_name,
                                        "type": folders_type,
                                        "label": _label,
                                        "sentences": text_raw
                                    }

                                    # Boost().multiprocessing(self.run, new_list_tools)

                                    Document().save(item)

                                f = {
                                    "type": folders_type,
                                    "label": _label,
                                    "doc": cont_doc
                                }

                                data.append(f)

                    log = {
                        "_id_dataset": _id_dataset,
                        "info": "Save Dataset.",
                        "data": data,
                        "data_time": datetime.datetime.now()
                    }

                elif files:
                    data = []
                    cont_doc = 0

                    for file_name in tqdm(os.listdir(path_dataset), desc="Document(s) save"):
                        cont_doc += 1

                        # open file
                        text_raw = Util().open_txt(path_dataset+"/"+file_name)

                        if (ssplit):
                            print(">> PreProcessing")
                            text_raw = self.ssplit(text_raw)
                            
                            item = {
                                "_id_dataset": _id_dataset,
                                "name": file_name,
                                "sentences": [sentence for sentence in text_raw ]
                                }

                        else:                
                            item = {
                                "_id_dataset": _id_dataset,
                                "name": file_name,
                                "sentences": text_raw
                                }
                        
                        Document().save(item)

                    data.append({"doc": cont_doc})

                    log = {
                        "_id_dataset": _id_dataset,
                        "info": "Save Datset.",
                        "data": data,
                        "data_time": datetime.datetime.now()
                    }
                
                #Logs().save(log)

        else:
            print("This path does not contain a valid directory!")
            sys.exit(0)

        return _id_dataset
