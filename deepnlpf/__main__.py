# -*- coding: utf-8 -*-
import argparse

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

    my_parser.version = '🐙 DeepNLPF v.0.0.2 α'

    my_parser.add_argument('--version',
                           help='show version.',
                           action='version')

    my_parser.add_argument('-install', '--install',
                        help="Command for install plugins.",
                        type=install,
                        action='store')

    args = my_parser.parse_args()

if __name__ == '__main__':
    main()
