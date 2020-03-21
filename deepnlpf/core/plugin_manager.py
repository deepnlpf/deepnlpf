#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Description:
    Date: 20/03/2020
"""

import os, sys, requests
from tqdm import tqdm

class PluginManager:

    def __init__(self):
        self.PATH_PLUGINS= os.environ['HOME'] + "/deepnlpf_plugins/"

    def load_plugin(self, plugin_name):
        directory, module_name = os.path.split(plugin_name)
        module_name = os.path.splitext(module_name)[0]

        path = list(sys.path)
        sys.path.insert(0, self.PATH_PLUGINS+plugin_name)

        try:
            module = __import__("plugin_%s" % module_name)
        finally:
            sys.path[:] = path # restore.
        return module

    def call_plugin(self, plugin_name, _id_pool, document, pipeline):
        plugin = self.load_plugin(plugin_name)
        return plugin.Plugin(_id_pool, document, pipeline).run()

    def download(self, plugin_name):
        # URL for download of plugin.
        URL_BEGIN = 'https://github.com/deepnlpf/'
        PLUGIN_NAME = 'plugin_stanfordcorenlp'
        URL_END = '/archive/master.zip'
        URL = URL_BEGIN + PLUGIN_NAME + URL_END 

        # Path for save plugin.
        HOME = os.environ['HOME']
        FOLDER_PLUGINS = '/deepnlpf_plugins/'
        PATH_DOWNLOAD_PLUGIN = HOME + FOLDER_PLUGINS + PLUGIN_NAME

        # check directory plugin exits else create.
        if not os.path.exists(HOME + FOLDER_PLUGINS):
            os.makedirs(HOME + FOLDER_PLUGINS)

        # download file
        r = requests.get(URL, stream=True)

        # Total size in bytes.
        total_size = int(r.headers.get('content-length', 0))
        block_size = 1024 # 1 Kibibyte

        # progress download.
        t = tqdm(total=total_size, unit='iB', unit_scale=True)

        # check download.
        with open(PATH_DOWNLOAD_PLUGIN+'.zip', 'wb') as f:
            for data in r.iter_content(block_size):
                t.update(len(data))
                f.write(data)
        t.close()

        if total_size != 0 and t.n != total_size:
            print("ERROR, something went wrong")