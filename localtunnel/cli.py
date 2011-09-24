# -*- coding: utf-8 -*-
"""
localtunnel.cli
~~~~~~~~~~~~~~~

This module provides the command-line interface for Localtunnel.
"""

import sys

import clint

USAGE = """
Usage: localtunnel [options] <localport>
    -k, --key FILE                   upload a public key for authentication
    -h, --help                       show this help
""".lstrip()


def display_usage():
    """Displays localtunnel usage."""

    print USAGE

def main():
    """Main localtunnel dispatch."""

    if ('-h', '--help') in clint.args:
        display_usage()
        sys.exit()

    elif ('-k', '--key') in clint.args:
        print 'importing key'
        sys.exit()

    elif not len(clint.args.not_flags):
        display_usage()
        sys.exit(1)

    port = clint.args.not_flags.pop(0)

if __name__ == '__main__':
    main()