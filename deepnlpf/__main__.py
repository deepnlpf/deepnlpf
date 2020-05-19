#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os

import deepnlpf._version as v
from deepnlpf.global_parameters import FILE_CONFIG


def config(args):
    from configparser import ConfigParser

    config = ConfigParser()
    config.read(FILE_CONFIG)

    debug = config.get("debug", "is_enabled")


def install(args):
    if args:
        from deepnlpf.core.plugin_manager import PluginManager

        PluginManager().install(args)
    else:
        print("❗️Wrong command!")
        print("⌨️ Try the command: deepnlpf --install <name_plugin>")


def uninstall(args):
    if args:
        from deepnlpf.core.plugin_manager import PluginManager

        PluginManager().uninstall(args)
    else:
        print("❗️Wrong command!")
        print("⌨️ Try the command: deepnlpf --uninstall <name_plugin>")


def listplugins(args):
    if args:
        from deepnlpf.core.plugin_manager import PluginManager

        PluginManager().listplugins(args)
    else:
        print("❗️Wrong command!")
        print("⌨️ Try the command: deepnlpf --listplugins all")


def api(args):
    if args == "start":
        os.system("cd deepnlpf/api && uvicorn main:app --reload")
    else:
        print("❗️Wrong command!")
        print("⌨️ Try the command: deepnlpf --api start")


def main():
    my_parser = argparse.ArgumentParser(
        prog="deepnlpf",
        description="⌨️  DeepNLPF Command Line Interface (CLI)",
        epilog="🐙 Enjoy the program! :)",
    )

    my_parser.version = "🐙 DeepNLPF V-" + v.__version__

    my_parser.add_argument("-v", "--version", help="show version.", action="version")

    my_parser.add_argument(
        "-i",
        "--install",
        help="Command for install plugin.",
        type=install,
        action="store",
    )

    my_parser.add_argument(
        "-u",
        "--uninstall",
        help="Command for uninstall plugin.",
        type=uninstall,
        action="store",
    )

    my_parser.add_argument(
        "-lp",
        "--listplugins",
        help="Command for listplugins plugin.",
        type=listplugins,
        action="store",
    )

    my_parser.add_argument(
        "-a", "--api", help="Command run api.", type=api, action="store"
    )

    my_parser.add_argument(
        "-c",
        "--config",
        help="Command config.",
        type=config,
        action="store",
        default=[]
    )

    args = my_parser.parse_args()


if __name__ == "__main__":
    main()
