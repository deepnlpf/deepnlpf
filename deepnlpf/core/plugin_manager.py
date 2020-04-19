#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, requests
import deepnlpf.log as log

from deepnlpf.core.util import Util

class PluginManager:

    def __init__(self):
        self.HOME = os.environ['HOME']

        self.PLUGIN_SERVER = 'https://rodriguesfas.com.br/deepnlpf/plugins/'
        self.PLUGIN_PATH = self.HOME + "/deepnlpf_data/plugins/"
        self.PLUGIN_EXTENSION = '.zip'

    def load_plugin(self, plugin_name):
        directory, module_name = os.path.split(plugin_name)
        module_name = os.path.splitext(module_name)[0]

        path = list(sys.path)
        sys.path.insert(0, self.PLUGIN_PATH+plugin_name)

        try:
            module = __import__("plugin_%s" % module_name)
        finally:
            sys.path[:] = path # restore.
        return module
    
    def load_manifest(self):
        file_manifest = 'manifest'
        plugins = []

        for plugin in os.listdir(self.PLUGIN_PATH):
            location = os.path.join(self.PLUGIN_PATH, plugin)
            if not os.path.isdir(location) or not file_manifest + ".json" in os.listdir(location):
                continue
            path = self.PLUGIN_PATH + '/' + plugin + '/' + file_manifest + ".json"
            plugins.append(Util().openfile_json(path))

        return plugins

    def call_plugin_nlp(self, plugin_name, _id_pool, lang, document, pipeline, **args):
        plugin = self.load_plugin(plugin_name)
        return plugin.Plugin(_id_pool, lang, document, pipeline).run()

    def call_plugin_db(self, plugin_name, operation, collection, document=None, key=None):
        plugin = self.load_plugin(plugin_name)
        log.logger.info("Plugin call: {}".format(plugin_name))

        if operation is 'insert':
            result = plugin.Plugin().insert(collection, document)
        elif operation is 'select_one':
            result = plugin.Plugin().select_one(collection, key)
        elif operation is 'select_all':
            result = plugin.Plugin().select_all(collection)
        elif operation is 'select_all_key':
            result = plugin.Plugin().select_all_key(collection, key)
        elif operation is 'update':
            result = plugin.Plugin().update(collection, key, document)
        elif operation is 'delete':
            result = plugin.Plugin().delete(collection, key)

        return result

    def install(self, plugin_name):
        import zipfile
        from homura import download # gestor fast download file. 

        # URL for download of plugin.
        URL = self.PLUGIN_SERVER + plugin_name + self.PLUGIN_EXTENSION

        # Path for save plugin.
        PATH_DOWNLOAD_PLUGIN = self.PLUGIN_PATH + plugin_name + self.PLUGIN_EXTENSION

        #check folder plugin exist.
        if not os.path.exists(self.PLUGIN_PATH):
            os.makedirs(self.PLUGIN_PATH)

        # Download plugin.
        print("Downloading plugin", plugin_name, "..")

        download(url=URL, path=PATH_DOWNLOAD_PLUGIN)

        try:
            # Extracting files plugin.
            fantasy_zip = zipfile.ZipFile(PATH_DOWNLOAD_PLUGIN)
            fantasy_zip.extractall(self.PLUGIN_PATH)
            fantasy_zip.close()
        except Exception as err:
            os.remove(PATH_DOWNLOAD_PLUGIN) # clear file zip.
            print("Plugin not found!")
            sys.exit(0)

        print("Plugin", plugin_name, "installed!")
        log.logger.info("Plugin installed: {}".format(plugin_name))
        print("Path of installed plugins:", self.HOME + FOLDER_PLUGINS)
        
        os.remove(PATH_DOWNLOAD_PLUGIN) # clear file zip.
        sys.exit(0)

    def uninstall(self, plugin_name):
        # Path for save plugin.
        FOLDER_PLUGINS = '/deepnlpf_data/plugins/'
        PATH_DOWNLOAD_PLUGIN = self.HOME + FOLDER_PLUGINS + plugin_name

        try:
            print("Uninstall plugin", plugin_name, "..")
            os.remove(PATH_DOWNLOAD_PLUGIN)
            print("Plugin", plugin_name, "unistalled!")
            log.logger.info("Plugin unistalled: {}".format(plugin_name))
        except Exception as err:
            print("Plugin not found!")

    def listplugins(self):
        # Path for save plugin.
        FOLDER_PLUGINS = '/deepnlpf_data/plugins/'
        pass
                


