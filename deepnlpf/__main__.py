#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os

import deepnlpf._version as v
from deepnlpf.global_parameters import FILE_CONFIG
from deepnlpf.config import Config

def set_toast(args):
    config = Config()
    config.set_notification_toast(args)
    status = config.get_notification_toast()
    print("Toast notification define:", status)

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
        "-st",
        "--settoast",
        help="Define status notification toast. [true|false]",
        type=set_toast,
        action="store"
    )

    args = my_parser.parse_args()


if __name__ == "__main__":
    main()
