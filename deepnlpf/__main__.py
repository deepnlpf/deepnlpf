# -*- coding: utf-8 -*-
import argparse, re
from os import path
from codecs import open

here = path.abspath(path.dirname(__file__))

def install(args):
    """Install
        install plugins in deepnlpf.
    """
    if args:
        from deepnlpf.core.plugin_manager import PluginManager
        PluginManager().download(args)
    else:
        print("Wrong command!")
        print("deepnlpf install <name_plugin>")

def main():
    my_parser = argparse.ArgumentParser(
        prog="deepnlpf",
        #usage='%(prog)s [argss] args',
        description="🐙 >>Command Line Interface.",
        epilog='🐙 >>Enjoy the program! :)'
    )

    version_file_contents = open(path.join(here, '_version.py'), encoding='utf-8').read()
    VERSION = re.compile('__version__ = \"(.*)\"').search(version_file_contents).group(1)
    my_parser.version = '🐙 DeepNLPF V' + VERSION

    my_parser.add_argument('-v', '--version',
                           help='show version.',
                           action='version')

    my_parser.add_argument('-install', '--install',
                        help="Command for install plugins.",
                        type=install,
                        action='store')

    args = my_parser.parse_args()

if __name__ == '__main__':
    main()
