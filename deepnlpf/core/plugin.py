#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Path: /deepnlpf/core/
    File: auto_load_plugin.py
    Class: AutoLoadPlugin
    Description:
    Date: 14/03/2019
"""

import imp
import os
import pathlib

from deepnlpf.core.util import Util
from deepnlpf.logs import logs


class PluginManager(object):

    PluginsFolder = "deepnlpf/plugins"
    MainModule = "__init__"
    file_manifest = "manifest"

    def collectPlugins(self):
        plugins = []
        possibleplugins = os.listdir(self.PluginsFolder)

        for plugin_name in possibleplugins:
            location = os.path.join(self.PluginsFolder, plugin_name)

            if not os.path.isdir(location) or not self.MainModule + ".py" in os.listdir(location):
                continue
            
            manifest = imp.find_module(self.MainModule, [location])

            # check plugin is activated.
            location = os.path.join(self.PluginsFolder, plugin_name)
            if not os.path.isdir(location) or not self.file_manifest + ".json" in os.listdir(location):
                continue
            path = self.PluginsFolder + '/' + plugin_name + '/' + self.file_manifest + ".json"
            info_manifest = Util().openfile_json(path)

            plugins.append({"name": plugin_name, "manifest": manifest})

        return plugins

    def loadPlugin(self, plugin):
        return imp.load_module(self.MainModule, *plugin["manifest"])

    def loadManifest(self):
        info_plugins = []
        possibleplugins = os.listdir(self.PluginsFolder)

        for plugin in possibleplugins:
            location = os.path.join(self.PluginsFolder, plugin)
            if not os.path.isdir(location) or not self.file_manifest + ".json" in os.listdir(location):
                continue
            path = self.PluginsFolder + '/' + plugin + '/' + self.file_manifest + ".json"
            info_plugins.append(Util().openfile_json(path))

        return info_plugins

    def getPlugins(self, list_tools):

        for plugin in self.collectPlugins():
            if plugin["name"] in list_tools: # check is plugin selected.
                try:
                    logs.logger.info("Loading plugin: " + plugin["name"])
                    p = self.loadPlugin(plugin)
                except Exception as err:
                    logs.logger.error("🐞 Loading plugin " + plugin["name"] + ": " + str(err))
