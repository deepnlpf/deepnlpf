#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib.request
import datetime
import validators

import pathos
import pathos.pools as pp
import psutil
import ray
from bson.objectid import ObjectId
from tqdm import tqdm

import deepnlpf.log as log
from deepnlpf.core.output_format import OutputFormat
from deepnlpf.core.plugin_manager import PluginManager
from deepnlpf.core.util import Util
from deepnlpf.global_parameters import *
from deepnlpf.notifications.toast import Toast
from deepnlpf.templates.schema import *
from deepnlpf.util.random_object_id import RandomObjectId


class Pipeline(object):

    RESULT = ""

    ID_DATASET = ""
    DOCUMENTS = ""
    DOCUMENTS_ANNOTATED = list()

    CPUS_COUNT: int = 0
    GPUS_COUNT: float = 0

    def __init__(
        self,
        _input: str,
        pipeline: str,
        _output: str = "terminal",
        _format: str = "json",
        use_db: str = None,
        tool_base: str = "stanza",
        boost: str = "ray",
        memory: int = None,
        num_cpus: int = 0,
        num_gpus: float = 0,
    ):

        self.toast = Toast()

        log.logger.info("--------------------- Start ---------------------")
        #self.toast.show("success", "DeepNLPF", "Start processing!")

        self._input = _input
        self._input_type = self.check_input_type_dataset(_input)

        self._pipeline = pipeline
        self._pipeline_type = self.check_input_format_pipeline(pipeline)
        self._custom_pipeline = self.load_file_pipeline(
            self._pipeline, self._pipeline_type
        )

        self._use_db = use_db
        log.logger.info("Use DB: {}".format(use_db))

        self._output = _output
        log.logger.info("Output: {}".format(_output))

        self._format = _format
        log.logger.info("Format: {}".format(_format))

        self._tool_base = tool_base
        log.logger.info("Tool NLP base: {}".format(tool_base))

        self._id_pool = ObjectId(b"foo-bar-quux")
        log.logger.info("Pool: {}".format(self._id_pool))

        self._boost = boost
        log.logger.info("Boost: {}".format(boost))

        self._memory = memory

        self.init_cpus(num_cpus)
        self.init_boost()

        self.GPUS_COUNT = num_gpus

    def init_cpus(self, cpus):
        """Initializes the CPUs

        Arguments:
            cpus {int} -- When this parameter is not defined [0], DeepNLP selects all 
                          CPUs present in the computer. Otherwise, select only the 
                          number of CPUs reported by the user.
        """
        if cpus == 0:
            self.CPUS_COUNT = psutil.cpu_count()  # get quant cpus device machine.
        else:
            self.CPUS_COUNT = cpus  # define quant cpus info user.

    def init_boost(self):
        """Starts the selected boost with the default or specified settings.
        """
        if self._boost == "pathos":
            self._id_pool = pp.ProcessPool(self.CPUS_COUNT)
        elif self._boost == "ray":
            ray.init(
                memory=self._memory, num_cpus=self.CPUS_COUNT, num_gpus=self.GPUS_COUNT
            )

    def check_input_type_dataset(self, _input: str) -> str:
        """Checks how the dataset is entered. [path_dataset|id_dataset|raw_text].

        Arguments:
            _input {str} -- The entry can be the dataset path, the dataset id or any text.

        Returns:
            str -- returns one of the following options: [path_dataset|id_dataset|raw_text]
        """
        try:
            result = ""

            if os.path.isdir(_input):
                result = INPUT_FORMAT_DATASET[0]  # path_dataset
            elif type(_input) == ObjectId:
                self.ID_DATASET = _input
                result = INPUT_FORMAT_DATASET[1]  # id_dataset
            elif type(_input) is str:
                result = INPUT_FORMAT_DATASET[2]  # raw_text
            else:
                print(
                    "Enter a parameter from a valid dataset [path_dataset|id_dataset|raw_text] ."
                )
                sys.exit(0)

            log.logger.info("Input data type: {}".format(result))
            return result
        except Exception as err:
            log.logger.error(err)
            sys.exit(0)

    def check_input_format_pipeline(self, pipeline: str) -> str:
        """Checks the file type of the pipeline.

        Arguments:
            pipeline {str} -- Pipeline file path.

        Returns:
            str -- File extension.
        """

        result = ""

        try:
            # check is file.
            if os.path.isfile(pipeline):
                file_name, ext = pipeline.split(".")
                result = (
                    ext.lower()
                )  # if the file extension was in capital letters it reduces to lower case.
            # check is url.
            elif validators.url(pipeline):
                result = "url"
            # check is json str
            elif json.loads(pipeline):
                result = "json_str"
            else:
                print(
                    "Enter a parameter from a valid pipeline {}.".format(
                        INPUT_FORMAT_PIPELINE
                    )
                )
                sys.exit(0)

            log.logger.info("Input pipeline type format: {}".format(result))

            return result
        except Exception as err:
            log.logger.error(err)
            sys.exit(0)

    def load_file_pipeline(self, pipeline: str, pipeline_type: str):
        """Load and convert the sent pipeline to Json..

        Arguments:
            pipeline {str} -- Path of the file containing the pipeline.
            pipeline_type {str} -- File type: [json, yaml, xml]

        Returns:
            {json} -- [The pipeline is always returned in Json format.]
        """
        try:
            result = ""

            if pipeline_type == "json":
                result = Util().openfile_json(pipeline)
            elif pipeline_type == "yaml":
                result = OutputFormat().yaml2json(pipeline)
            elif pipeline_type == "xml":
                result = OutputFormat().xml2json(pipeline)
            elif pipeline_type == "url":
                with urllib.request.urlopen(pipeline) as url:
                    result = json.loads(url.read().decode())
            elif pipeline_type == "json_str":
                result = json.loads(pipeline)

            log.logger.info("Custom Pipeline: {}".format(result))
            return result
        except Exception as err:
            log.logger.error(err)
            sys.exit(0)

    def load_dataset(self, _input_type):
        """Loads data from the dataset.

        Arguments:
            _input_type {string} -- If _input_type [path_dataset] it is understood that 
                                    the data are in text files and must be accurately checked, 
                                    preprocessed and organized before processing.

                                    If _input_type [id_dataset] it is understood that the data 
                                    must be loaded from a local database.

                                    iF _input_type [raw_text] it is understood that the data to 
                                    be loaded is any text and needs to be checked, pre-processed 
                                    and organized before processing.

        Returns:
            {list} -- returns a list containing the dataset id, and the documents to be processed.
        """

        # path_dataset
        if _input_type == INPUT_FORMAT_DATASET[0]:
            return self.prepare_dataset()
        # id_dataset
        elif _input_type == INPUT_FORMAT_DATASET[1]:
            return self.load_database(
                database_name=self._use_db, id_dataset=self._input
            )
        # raw_text
        elif _input_type == INPUT_FORMAT_DATASET[2]:
            documents = self.prepare_raw_text(self._input)
            return documents

    def annotate(self):

        self.DOCUMENTS = self.load_dataset(self._input_type)

        log.logger.info(
            "Number of documents to process: {}".format(len(self.DOCUMENTS))
        )

        # get tools names
        list_tools = [tool for tool, _ in self._custom_pipeline["tools"].items()]

        if self._boost == "pathos":
            process = str(pathos.helpers.mp.current_process())
            log.logger.info("{}".format(process))

            self.RESULT = [
                _
                for _ in tqdm(
                    self._id_pool.map(self.run, list_tools),
                    total=len(list_tools),
                    desc="NLP Tool(s)",
                )
            ]

        elif self._boost == "ray":

            @ray.remote
            def f(tool):
                log.logger.info("Plugin Tool: {}".format(tool))
                self.run(tool)

            # Start N task in parallel.
            futures = [f.remote(tool) for tool in list_tools]

            self.RESULT = ray.get(futures)

        log.logger.info("--------------------- End ---------------------")
        #self.toast.show("success", "DeepNLPF", "End processing.")

        if self._output == "file":
            return {
                "results": os.environ["HOME"]
                + "/deepnlpf_data/output/dataset_"
                + str(self.ID_DATASET)
            }
        else:
            return self.RESULT

    def run(self, tool):

        for document in tqdm(self.DOCUMENTS, desc="Document(s)"):

            annotated_document = PluginManager().call_plugin_nlp(
                plugin_name=tool,
                document=document["sentences"],
                pipeline=self._custom_pipeline,
            )

            # validates document annotated by the tool.
            validate_annotation(annotated_document)

            if self._use_db != None:
                PluginManager().call_plugin_db(
                    plugin_name=self._use_db,
                    operation="insert",
                    collection="analysi",
                    document={
                        "_id_dataset": self.ID_DATASET,
                        "_id_document": document["_id"],
                        "_id_pool": self._id_pool,
                        "tool": tool,
                        "sentences": annotated_document,
                    },
                )

            data_formating = {"sentences": annotated_document}

            # add document annotated in list documents.
            self.DOCUMENTS_ANNOTATED.append(
                self.type_output_results(
                    data_formating, self.ID_DATASET, document["name"], tool,
                )
            )

        return self.DOCUMENTS_ANNOTATED

    def load_database(self, database_name, id_dataset):
        """Load documents from a database.

        Arguments:
            database_name {str} -- Name of the database being used.
            id_dataset {str} -- Dataset id saved in the database.

        Returns:
            [type] -- A list of documents to be processed.
        """
        results = PluginManager().call_plugin_db(
            plugin_name=database_name,
            operation="select_all_key",
            collection="document",
            key={"_id_dataset": ObjectId(id_dataset)},
        )

        return results

    def type_output_file(self, annotation):
        if self._format == "xml":
            return OutputFormat().json2xml(annotation)
        elif self._format == "json":
            return annotation

    def type_output_results(self, annotation, _id_dataset, _id_document, plugin_name):
        if self._output == "terminal":
            return annotation

        elif self._output == "file":
            EXT = ".xml" if self._format == "xml" else ".json"

            # Create dir name dataset.
            PATH_DATASET = (
                os.environ["HOME"] + "/deepnlpf_data/output/dataset_" + str(_id_dataset)
            )

            PATH_DOCUMENT = (
                os.environ["HOME"]
                + "/deepnlpf_data/output/dataset_"
                + str(_id_dataset)
                + "/"
                + _id_document
            )

            if not os.path.exists(PATH_DATASET):
                os.makedirs(PATH_DATASET)

            if not os.path.exists(PATH_DOCUMENT):
                os.makedirs(PATH_DOCUMENT)

            # save file document(s).
            PATH = (
                os.environ["HOME"]
                + "/deepnlpf_data/output/dataset_"
                + str(_id_dataset)
                + "/"
                + _id_document
                + "/"
                + plugin_name
                + EXT
            )
            Util().save_file(PATH, str(annotation))
            log.logger.info("Output file in: {}".format(PATH))

        elif self._output == "browser":
            from flask import Flask, escape, request

            app = Flask(__name__)

            @app.route("/")
            def hello():
                name = request.args.get("name", annotation)
                return f"Hello, {escape(name)}!"

            app.run(debug=True)

    def prepare_raw_text(self, raw_text):
        log.logger.info("Pre-processing - Execute Sentence Split in texto raw.")

        list_sentences = list()

        # pre-processing tokenization and ssplit using plugin base selected.
        if self._tool_base == "stanza":
            doc_annotation = PluginManager().call_plugin_nlp(
                plugin_name="preprocessing",
                document=raw_text,
                pipeline={
                    "lang": self._custom_pipeline["lang"],
                    "tools": {"stanza": {"processors": ["tokenize"]}},
                },
            )

            # join tokens.
            for sentence in doc_annotation.sentences:
                list_tokens = list()
                for token in sentence.tokens:
                    list_tokens.append(token.text)
                list_sentences.append(" ".join(list_tokens))

        if self._tool_base == "stanfordcorenlp":
            doc_annotation = PluginManager().call_plugin_nlp(
                plugin_name="preprocessing",
                document=raw_text,
                pipeline={
                    "lang": self._custom_pipeline["lang"],
                    "tools": {"stanfordcorenlp": {"processors": ["ssplit"]}},
                },
            )

            for item in doc_annotation[0]["sentences"]:
                sentence = list()
                for token in item["tokens"]:
                    sentence.append(token["word"])
                list_sentences.append(" ".join(sentence))

        if self._use_db != None:
            # insert dataset in database.
            self.ID_DATASET = PluginManager().call_plugin_db(
                plugin_name=self._use_db,
                operation="insert",
                collection="dataset",
                document={
                    "name": "dataset_" + RandomObjectId().gen_random_object_id_string(),
                    "data_time": OutputFormat().data_time(),
                },
            )

            # insert document(s) in database.
            PluginManager().call_plugin_db(
                plugin_name=self._use_db,
                operation="insert",
                collection="document",
                document={
                    "_id_dataset": self.ID_DATASET,
                    "name": "document_"
                    + RandomObjectId().gen_random_object_id_string(),
                    "sentences": [sentence for sentence in list_sentences],
                },
            )

            return self.get_all_documents_database()

        # Not using database.
        else:
            # generates a document id.
            _id = RandomObjectId().gen_random_object_id()

            # generate an id for the dataset.
            self.ID_DATASET = RandomObjectId().gen_random_object_id()

            # generates a name for the document.
            name = "document_" + RandomObjectId().gen_random_object_id_string()

            document = {
                "_id": _id,
                "_id_dataset": self.ID_DATASET,
                "name": name,
                "sentences": list_sentences,
            }

            return [document]

    def get_all_documents_database(self):
        self.DOCUMENTS = PluginManager().call_plugin_db(
            plugin_name=self._use_db,
            operation="select_all_key",
            collection="document",
            key={"_id_dataset": ObjectId(self.ID_DATASET)},
        )
        return self.DOCUMENTS

    def prepare_dataset(self):
        """Prepare the supplied dataset to be processed.

        Returns:
            {list} -- Returns a list of documents to be processed.
        """

        path_dataset = self._input
        dataset_name = ""
        list_documents = list()
        log_document = ""

        # check is path directory validate.
        if os.path.isdir(path_dataset):
            # check whether the directory is empty.
            if os.listdir(path_dataset) == []:
                print("Directory empty!")
                sys.exit(0)
            # if the directory is not empty.
            else:
                # takes the name of the directory and names the dataset.
                dataset_name = os.path.basename(os.path.normpath(path_dataset))

                # if using database save dataset.
                if self._use_db != None:
                    self.ID_DATASET = PluginManager().call_plugin_db(
                        plugin_name=self._use_db,
                        operation="insert",
                        collection="dataset",
                        document={
                            "name": dataset_name,
                            "data_time": datetime.datetime.now(),
                        },
                    )
                # if you are not using a database, generate an id for the dataset.
                else:
                    self.ID_DATASET = RandomObjectId().gen_random_object_id()

                # get all files' and directorys' names in the current directory.
                dirrectory_contents = os.listdir(path_dataset)

                list_files = []
                list_sub_directory = []  # train or test.

                # check all directory contents
                for item in dirrectory_contents:
                    # check whether the current item is a sub directory and add the list sub directory.
                    if os.path.isdir(os.path.join(os.path.abspath(path_dataset), item)):
                        list_sub_directory.append(item)
                    # make sure the current item is a file and add the file list.
                    elif os.path.isfile(
                        os.path.join(os.path.abspath(path_dataset), item)
                    ):
                        list_files.append(item)

                # check exist sub directory.
                if list_sub_directory != []:
                    data = []

                    for directory_type in list_sub_directory:
                        print("├── {}:".format(directory_type))

                        folders_labels = os.listdir(path_dataset + "/" + directory_type)

                        for _label in folders_labels:
                            cont_doc = 0

                            if os.path.isdir(
                                os.path.join(
                                    os.path.abspath(
                                        path_dataset + "/" + directory_type
                                    ),
                                    _label,
                                )
                            ):

                                for file_name in tqdm(
                                    os.listdir(
                                        path_dataset
                                        + "/"
                                        + directory_type
                                        + "/"
                                        + _label
                                        + "/"
                                    ),
                                    desc="│   └── documents [{}]".format(_label),
                                ):
                                    cont_doc += 1

                                    text_raw = Util().open_txt(
                                        path_dataset
                                        + "/"
                                        + directory_type
                                        + "/"
                                        + _label
                                        + "/"
                                        + file_name
                                    )

                                    document = {
                                        "_id_dataset": self.ID_DATASET,
                                        "name": file_name,
                                        "type": directory_type,
                                        "label": _label,
                                        "sentences": text_raw,
                                    }

                                    if self._use_db != None:
                                        PluginManager().call_plugin_db(
                                            plugin_name=self._use_db,
                                            operation="insert",
                                            collection="document",
                                            document=document,
                                        )

                                f = {
                                    "type": directory_type,
                                    "label": _label,
                                    "doc": cont_doc,
                                }

                                data.append(f)

                    log = {
                        "_id_dataset": self.ID_DATASET,
                        "info": "Save Dataset.",
                        "data": data,
                        "data_time": datetime.datetime.now(),
                    }

                elif list_files != []:
                    data = []
                    cont_doc = 0

                    for file_name in tqdm(
                        os.listdir(path_dataset), desc="Document(s) save"
                    ):
                        cont_doc += 1

                        # open file
                        text_raw = Util().open_txt(path_dataset + "/" + file_name)

                        # if text raw.
                        if self._input_type == INPUT_FORMAT_DATASET[2]:
                            text_raw = self.prepare_raw_text(text_raw)

                            item = {
                                "_id_dataset": self.ID_DATASET,
                                "name": file_name,
                                "sentences": [sentence for sentence in text_raw],
                            }
                        # is file.
                        else:
                            if self._use_db != None:
                                document_document = {
                                    "_id_dataset": self.ID_DATASET,
                                    "name": file_name,
                                    "sentences": text_raw,
                                }

                                PluginManager().call_plugin_db(
                                    plugin_name=self._use_db,
                                    operation="insert",
                                    collection="document",
                                    document=document_document,
                                )
                            else:
                                list_documents.append(
                                    {
                                        "_id": RandomObjectId().gen_random_object_id_string(),
                                        "_id_dataset": self.ID_DATASET,
                                        "name": file_name,
                                        "sentences": text_raw,
                                    }
                                )

                    data.append({"doc": cont_doc})

                    if self._use_db != None:
                        log_document = {
                            "_id_dataset": self.ID_DATASET,
                            "info": "Save Dataset.",
                            "data": data,
                            "data_time": datetime.datetime.now(),
                        }

                if self._use_db != None:
                    PluginManager().call_plugin_db(
                        plugin_name=self._use_db,
                        operation="insert",
                        collection="log",
                        document=log_document,
                    )

        else:
            print("This path does not contain a valid directory!")
            sys.exit(0)

        return list_documents
