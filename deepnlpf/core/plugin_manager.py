#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import deepnlpf.log as log
from deepnlpf.core.util import Util


class PluginManager:
    def __init__(self):
        self.HOME = os.environ["HOME"]
        self.PLUGIN_SERVER = "https://github.com/deepnlpf/"
        self.PLUGIN_PATH = self.HOME + "/deepnlpf_data/plugins/"
        self.EXTENSION = ".zip"

    def load_plugin(self, plugin_name):
        directory, module_name = os.path.split(plugin_name)
        module_name = os.path.splitext(module_name)[0]

        path = list(sys.path)
        sys.path.insert(0, self.PLUGIN_PATH + plugin_name)

        try:
            module = __import__("plugin_%s" % module_name)
        finally:
            sys.path[:] = path  # restore.
        return module

    def load_manifest(self):
        file_manifest = "manifest"
        plugins = []

        for plugin in os.listdir(self.PLUGIN_PATH):
            location = os.path.join(self.PLUGIN_PATH, plugin)
            if not os.path.isdir(location) or not file_manifest + ".json" in os.listdir(
                location
            ):
                continue
            path = self.PLUGIN_PATH + "/" + plugin + "/" + file_manifest + ".json"
            plugins.append(Util().openfile_json(path))

        return plugins

    def call_plugin_nlp(self, plugin_name, document, pipeline):
        plugin = self.load_plugin(plugin_name)
        return plugin.Plugin(document, pipeline).run()

    def call_plugin_db(
        self, plugin_name, operation, collection, document=None, key=None
    ):
        plugin = self.load_plugin(plugin_name)
        log.logger.info("Plugin call: {}".format(plugin_name))

        if operation == "insert":
            result = plugin.Plugin().insert(collection, document)
        elif operation == "select_one":
            result = plugin.Plugin().select_one(collection, key)
        elif operation == "select_all":
            result = plugin.Plugin().select_all(collection)
        elif operation == "select_all_key":
            result = plugin.Plugin().select_all_key(collection, key)
        elif operation == "update":
            result = plugin.Plugin().update(collection, key, document)
        elif operation == "delete":
            result = plugin.Plugin().delete(collection, key)

        return result

    def install(self, plugin_name):
        import zipfile
        from homura import download  # gestor fast download file.

        # URL for download of plugin.
        # https://github.com/deepnlpf/plugin_stanza/archive/master.zip
        URL = (
            self.PLUGIN_SERVER
            + "plugin_"
            + plugin_name
            + "/archive/master"
            + self.EXTENSION
        )

        # Path for save plugin.
        PATH_DOWNLOAD_PLUGIN = (
            self.PLUGIN_PATH + "plugin_" + plugin_name + "-master" + self.EXTENSION
        )

        # check folder plugin exist.
        if not os.path.exists(self.PLUGIN_PATH):
            os.makedirs(self.PLUGIN_PATH)

        # Download plugin.
        try:
            print("Downloading plugin", plugin_name, "..")
            # check url exists.
            download(url=URL, path=PATH_DOWNLOAD_PLUGIN)
        except Exception as err:
            print("❗️Plugin no found!")
            log.logger.error(err)
            sys.exit(0)

        # Extracting files plugin.
        try:
            fantasy_zip = zipfile.ZipFile(PATH_DOWNLOAD_PLUGIN)
            fantasy_zip.extractall(self.PLUGIN_PATH)
            fantasy_zip.close()
        except Exception as err:
            print("❗️Error extracting files!")
            log.logger.error(err)
            sys.exit(0)

        # Config dir name plugin.
        try:
            os.rename(
                self.PLUGIN_PATH + "plugin_" + plugin_name + "-master",
                self.PLUGIN_PATH + plugin_name,
            )
        except Exception as err:
            print("❗️Error config directory plugin!")
            log.logger.error(err)
            sys.exit(0)

        # Install requirements.
        try:
            # Check in plugin file requirements.sh exist.
            if os.path.isfile(self.PLUGIN_PATH + plugin_name + "/requeriments.sh"):
                print("Install requirements..")
                os.system(
                    "cd "
                    + str(
                        self.PLUGIN_PATH
                        + plugin_name
                        + " && chmod 777 requeriments.sh && ./requeriments.sh"
                    )
                )
        except Exception as err:
            print("❗Error when executing the requeriments.sh plugin file!")
            log.logger.error(err)
            sys.exit(0)

        os.remove(PATH_DOWNLOAD_PLUGIN)  # clear file zip.
        print("🎉 Plugin", plugin_name, "installed!")
        log.logger.info("Plugin installed: {}".format(plugin_name))
        print("Path of installed plugins:", self.PLUGIN_PATH)
        sys.exit(0)

    def uninstall(self, plugin_name):
        # Path for save plugin.
        PATH_DOWNLOAD_PLUGIN = self.HOME + self.PLUGIN_PATH + plugin_name

        try:
            print("Uninstall plugin", plugin_name, "..")
            os.remove(PATH_DOWNLOAD_PLUGIN)
            print("Plugin", plugin_name, "unistalled!")
            log.logger.info("Plugin unistalled: {}".format(plugin_name))
        except Exception as err:
            log.logger.error(err)
            print("Plugin not found!")

    def listplugins(self):
        # Path for save plugin.
        pass
