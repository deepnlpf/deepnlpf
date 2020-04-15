#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Description:
    Date: 20/03/2020
"""

from deepnlpf.core.util import Util
import os, sys, requests

class PluginManager:

    def __init__(self):
        self.PATH_PLUGINS = os.environ['HOME'] + "/deepnlpf_data/plugins/"

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
    
    def load_plugin_manifest(self):
        file_manifest = 'manifest'
        plugins = []

        for plugin in os.listdir(self.PATH_PLUGINS):
            location = os.path.join(self.PATH_PLUGINS, plugin)
            if not os.path.isdir(location) or not file_manifest + ".json" in os.listdir(location):
                continue
            path = self.PATH_PLUGINS + '/' + plugin + '/' + file_manifest + ".json"
            plugins.append(Util().openfile_json(path))

        return plugins

    def call_plugin(self, plugin_name, _id_pool, lang, document, pipeline, **args):
        plugin = self.load_plugin(plugin_name)
        return plugin.Plugin(_id_pool, lang, document, pipeline).run()

    def call_plugin_db(self, plugin_name, operation, collection, document=None, key=None):
        plugin = self.load_plugin(plugin_name)

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
        URL_BEGIN = 'https://rodriguesfas.com.br/deepnlpf/plugins/'
        PLUGIN_NAME = plugin_name
        EXTENSION = '.zip'
        URL = URL_BEGIN + PLUGIN_NAME + EXTENSION 

        # Path for save plugin.
        HOME = os.environ['HOME']
        FOLDER_PLUGINS = '/deepnlpf_data/plugins/'
        PATH_DOWNLOAD_PLUGIN = HOME + FOLDER_PLUGINS + PLUGIN_NAME + EXTENSION

        #check folder plugin exist.
        if not os.path.exists(HOME + FOLDER_PLUGINS):
            os.makedirs(HOME + FOLDER_PLUGINS)

        # Download plugin.
        print("Downloading plugin", PLUGIN_NAME, "..")

        download(url=URL, path=PATH_DOWNLOAD_PLUGIN)

        try:
            # Extracting files plugin.
            fantasy_zip = zipfile.ZipFile(PATH_DOWNLOAD_PLUGIN)
            fantasy_zip.extractall(HOME + FOLDER_PLUGINS)
            fantasy_zip.close()
        except Exception as err:
            os.remove(PATH_DOWNLOAD_PLUGIN) # clear file zip.
            print("Plugin not found!")
            sys.exit(0)

        print("Plugin", PLUGIN_NAME, "installed!")
        print("Path of installed plugins:", HOME + FOLDER_PLUGINS)
        
        os.remove(PATH_DOWNLOAD_PLUGIN) # clear file zip.
        sys.exit(0)

    def uninstall(self, plugin_name):
        # Path for save plugin.
        HOME = os.environ['HOME']
        PLUGIN_NAME = plugin_name
        FOLDER_PLUGINS = '/deepnlpf_data/plugins/'
        PATH_DOWNLOAD_PLUGIN = HOME + FOLDER_PLUGINS + PLUGIN_NAME

        try:
            print("Uninstall plugin", PLUGIN_NAME, "..")
            os.remove(PATH_DOWNLOAD_PLUGIN)
            print("Plugin", PLUGIN_NAME, "unistalled!")
        except Exception as err:
            print("Plugin not found!")

    def listplugins(self):
        # Path for save plugin.
        HOME = os.environ['HOME']
        FOLDER_PLUGINS = '/deepnlpf_data/plugins/'
        PATH_DOWNLOAD_PLUGIN = HOME + FOLDER_PLUGINS
        pass
                


