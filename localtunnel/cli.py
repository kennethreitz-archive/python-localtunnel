# -*- coding: utf-8 -*-
"""
localtunnel.cli
~~~~~~~~~~~~~~~

This module provides the command-line interface for Localtunnel.
"""

import sys

import clint
from clint.arguments import _expand_path as expand_path

USAGE = '''
Usage: localtunnel [options] <localport>
    -k, --key FILE                   upload a public key for authentication
    -h, --help                       show this help
'''.lstrip()

PORT_ERROR = 'Invalid port number.'

def display_usage():
    """Displays localtunnel usage."""
    print USAGE

def display_port_error():
    print PORT_ERROR


def main():
    """Main localtunnel dispatch."""

    if ('-h', '--help') in clint.args:
        display_usage()
        sys.exit()

    elif ('-k', '--key') in clint.args:
        print 'importing key'
        # print clint.args.files
        print expand_path('~/ssh/*.pub')
        sys.exit()

    elif not len(clint.args.not_flags):
        display_usage()
        sys.exit(1)

    port = clint.args.not_flags.pop(0)

    try:
        int(port)
    except ValueError:
        display_port_error()
        sys.exit(1)

if __name__ == '__main__':
    main()