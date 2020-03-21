#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Date: 07/03/2019
"""

import os, json, datetime

from tqdm import tqdm

from deepnlpf.config import config

from deepnlpf.models.logs import Logs
from deepnlpf.models.dataset import Dataset
from deepnlpf.models.document import Document

from deepnlpf.core.boost import Boost

class Util(object):

    def __init__(self):
        pass

    def save_dataset(self, path_dataset, ssplit=False):
        dataset_name = ''

        # check is path dir validate.
        if(os.path.isdir(path_dataset)):
            # check if folder empty
            if os.listdir(path_dataset) == []:
                print('Folder empty!')
            else:
                # get name corpus
                dataset_name = os.path.basename(os.path.normpath(path_dataset))
                    
                # save corpus
                _id_dataset = Dataset().save({
                    "name": dataset_name,
                    "last_modified": datetime.datetime.now()
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

                                for doc_name in tqdm(os.listdir(path_dataset+"/"+folders_type+"/"+_label+"/"), desc="│   └── documents [{}]".format(_label)):
                                    cont_doc += 1

                                    text_raw = Util().open_txt(path_dataset+"/"+folders_type+"/"+_label+"/"+doc_name)
                                    
                                    # Sentence Split.
                                    #sentences = PreProcessing('ssplit', text_raw).run()

                                    item = {
                                        "_id_dataset": _id_dataset,
                                        "name": doc_name,
                                        "type": folders_type,
                                        "label": _label,
                                        "sentences": text_raw
                                    }

                                    # Boost().parallelpool(self.run, new_list_tools)

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
                        "last_modified": datetime.datetime.now()
                    }

                elif files:
                    data = []
                    cont_doc = 0

                    for doc_name in os.listdir(path_dataset):
                        cont_doc += 1

                        text_raw = Util().open_txt(path_dataset+"/"+doc_name)

                        if (ssplit):
                            print(">> PreProcessing")
                            text_raw = PreProcessing('ssplit', text_raw).run()
                            
                            item = {
                                "_id_dataset": _id_dataset,
                                "name": doc_name,
                                "sentences": [sentence for sentence in text_raw ]
                                }

                        else:                
                            item = {
                                "_id_dataset": _id_dataset,
                                "name": doc_name,
                                "sentences": text_raw
                                }
                        
                        Document().save(item)

                    data.append({"doc": cont_doc})

                    log = {
                        "_id_dataset": _id_dataset,
                        "info": "Save Datset.",
                        "data": data,
                        "last_modified": datetime.datetime.now()
                    }
                
                Logs().save(log)

        else:
            print("This path does not contain a valid directory!")

        return {
            'dataset_name': dataset_name,
            'dataset_id': _id_dataset
        }

    def openfile_json(self, path_file):
        try:
            with open(path_file, 'r') as file:
                return json.load(file)
        except Exception as err:
            return "Error loading file!" + err

    def open_txt(self, path_file):
        data_temp = []
        
        try:
            with open(path_file) as file:
                for line in file:
                    data_temp.append(line.strip())
                return data_temp
        except Exception as err:
            return "Error loading file!" + str(err)

    def save_txt(self, path_file, corpus):
        try:
            temp_file = open(path_file, 'w')
        
            for line in corpus:
                temp_file.write(line+"\n")

            temp_file.close()
        except Exception as err:
            print(err)

    def save_json(self, path_file, corpus):
        try:
            temp_file = open(path_file, 'w')
        
            for line in corpus:
                temp_file.write(line+"\n")

            temp_file.close()
        except Exception as err:
            print(err)