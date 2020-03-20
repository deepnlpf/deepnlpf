#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Description:
    Date: 20/03/2020
"""

import os, sys

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