# -*- coding: utf-8 -*-

import os, sys, argparse, datetime

from os import walk
from tqdm import tqdm

from deepnlpf.config import config
from deepnlpf.models.logs import Logs
from deepnlpf.models.dataset import Dataset
from deepnlpf.models.document import Document
from deepnlpf.core.util import Util

from deepnlpf.core.boost import Boost
from deepnlpf.pipeline import Annotation
from deepnlpf.core.preprocessing import PreProcessing

def server(args):
    # TODO Remover IP e Port daqui e colocar em um aqruivo de configuração.
    from deepnlpf.server import app, socketio

    if(args == 'start'):
        socketio.run(app, host=config.CONFIG['host'], port=config.CONFIG['port_server'])
    else:
        print("wrong argument!")


def dashboard(args):
    from deepnlpf.client.app import app

    if(args == 'start'):
        app.run(host=config.CONFIG['host'], port=config.CONFIG['port_dashboard'])
    else:
        print("wrong argument!")


# TODO listar os plugins com sua respectiva versão.
def plugins(args):
    if(args == "all"):
        all_plugins = os.listdir('deepnlpf/plugins/')
        for plugin in all_plugins:
            print(plugin)
    else:
        print("wrong argument!")


def pipeline(args):
    custom_pipeline = Util().openfile_json(args)
    corpus_id = custom_pipeline['corpus_id']

    annotation = Annotation(corpus_id, custom_pipeline, True)
    request = annotation.annotate()


def statistics():
    print("Run statistics!")


def savecorpus(args):
    path_corpus = args

    # check is path dir validate.
    if(os.path.isdir(path_corpus)):
        # check if folder empty
        if os.listdir(path_corpus) == []:
            print('Folder empty!')
        else:
            # get name corpus
            corpus_name = os.path.basename(os.path.normpath(path_corpus))
                
            # save corpus
            _id_dataset = Dataset().save({
                "name": corpus_name,
                "last_modified": datetime.datetime.now()
            })
            
            print("corpus: {}".format(corpus_name))

            # get all files' and folders' names in the current directory.
            dirContents = os.listdir(path_corpus)

            files = []
            subfolders = [] # train or test.

            for filename in dirContents:
                # check whether the current object is a folder or not.
                if os.path.isdir(os.path.join(os.path.abspath(path_corpus), filename)):
                    subfolders.append(filename)
                elif os.path.isfile(os.path.join(os.path.abspath(path_corpus), filename)):
                    files.append(filename)

            if subfolders: # check exist folders
                data = []

                for folders_type in subfolders:
                    print("├── {}:".format(folders_type))

                    folders_labels = os.listdir(path_corpus+"/"+folders_type)

                    for _label in folders_labels:
                        cont_doc = 0

                        if os.path.isdir(os.path.join(os.path.abspath(path_corpus+"/"+folders_type), _label)):

                            for doc_name in tqdm(os.listdir(path_corpus+"/"+folders_type+"/"+_label+"/"), desc="│   └── documents [{}]".format(_label)):
                                cont_doc += 1

                                text_raw = Util().open_txt(path_corpus+"/"+folders_type+"/"+_label+"/"+doc_name)
                                
                                # Sentence Split
                                #sentences = PreProcessing('ssplit', text_raw).run()

                                item = {
                                    "_id_dataset": _id_dataset,
                                    "name": doc_name,
                                    "type": folders_type,
                                    "label": _label,
                                    "sentences": text_raw
                                }

                                Document().save(item)

                            f = {
                                "type": folders_type,
                                "label": _label,
                                "doc": cont_doc
                            }

                            data.append(f)

                log = {
                    "_id_dataset": _id_dataset,
                    "info": "Save corpus.",
                    "data": data,
                    "last_modified": datetime.datetime.now()
                }

            elif files:
                data = []
                cont_doc = 0

                for doc_name in os.listdir(path_corpus):
                    cont_doc += 1

                    text_raw = Util().open_txt(path_corpus+"/"+doc_name)
                    sentences = PreProcessing('ssplit', text_raw).run()

                    item = {
                        "_id_dataset": _id_dataset,
                        "name": doc_name,
                        "sentences": text_raw
                    }

                    #Document().save(item)
                    Document().save(item)

                data.append({"doc": cont_doc})

                log = {
                    "_id_dataset": _id_dataset,
                    "info": "Save corpus.",
                    "data": data,
                    "last_modified": datetime.datetime.now()
                }
            
            Logs().save(log)
            print("└── _id_dataset:", _id_dataset)

    else:
        print("This path does not contain a valid directory!")


def listcorpus(args):
    for item in Dataset().select_all():
        print("├──Corpus:", item['name'])
        print("│  ID:", item['_id'])
        print("│  Register", item['last_modified'])
        print("__________________________________")

def deletecorpus(args):
    print(Dataset().delete(args))


def main():
    my_parser = argparse.ArgumentParser(
        prog="deepnlpf",
        #usage='%(prog)s [argss] args',
        description="🐙 >>Command Line Interface.",
        epilog='🐙 >>Enjoy the program! :)'
    )

    my_parser.version = '🐙 DeepNLPF v.0.0.2 α'

    my_parser.add_argument('--server',
                           help="run server.",
                           type=server,
                           action="store")

    my_parser.add_argument('--dashboard',
                           help="run dashboard.",
                           type=dashboard,
                           action="store")

    my_parser.add_argument('--version',
                           help='show version.',
                           action='version')

    my_parser.add_argument('--plugins',
                           help="list all plugins install.",
                           type=plugins,
                           action='store')

    my_parser.add_argument('--pipeline',
                           metavar='path_file_custom_pipeline',
                           help="run pipeline analise.",
                           type=pipeline,
                           action='store')

    my_parser.add_argument('--statistics',
                           metavar='corpus_id',
                           help="generate statistics corpus.",
                           type=statistics,
                           action='store')

    my_parser.add_argument('--savecorpus',
                           metavar='path_dir_corpus',
                           help="save corpus in database.",
                           type=savecorpus,
                           action='store')

    my_parser.add_argument('--listcorpus',
                           help="list all corpus.",
                           type=listcorpus,
                           action='store')

    my_parser.add_argument('--deletecorpus',
                           help="delete specific corpus.",
                           type=deletecorpus,
                           action='store')

    # Execute parse_args()
    args = my_parser.parse_args()


if __name__ == '__main__':
    main()
