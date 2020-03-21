#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Description:
    Date: 20/03/2020
"""

import os, sys, requests

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
        import zipfile
        from homura import download

        # URL for download of plugin.
        URL_BEGIN = 'https://rodriguesfas.com.br/deepnlpf/plugins/'
        PLUGIN_NAME = plugin_name
        EXTENSION = '.zip'
        URL = URL_BEGIN + PLUGIN_NAME + EXTENSION 

        # Path for save plugin.
        HOME = os.environ['HOME']
        FOLDER_PLUGINS = '/deepnlpf_plugins/'
        PATH_DOWNLOAD_PLUGIN = HOME + FOLDER_PLUGINS + PLUGIN_NAME + EXTENSION

        try:
            #check folder plugin exist.
            if not os.path.exists(HOME + FOLDER_PLUGINS):
                os.makedirs(HOME + FOLDER_PLUGINS)

            # Download plugin.
            print("Downloading the plugin", PLUGIN_NAME, "..")
            download(url=URL, path=PATH_DOWNLOAD_PLUGIN)
        except Exception as err:
            print("Plugin no exist!")
            print(err)
            sys.exit(0)

        try:
            # Extracting files plugin.
            fantasy_zip = zipfile.ZipFile(PATH_DOWNLOAD_PLUGIN)
            fantasy_zip.extractall(HOME + FOLDER_PLUGINS)
            fantasy_zip.close()
        except Exception as err:
            print("Err extraction file!")
            print(err)

        os.remove(PATH_DOWNLOAD_PLUGIN) # clear file zip.

        print("Plugin", PLUGIN_NAME, "intalled!")
        print("Path of installed plugins:", HOME + FOLDER_PLUGINS)

        


