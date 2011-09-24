# -*- coding: utf-8 -*-
"""
localtunnel.cli
~~~~~~~~~~~~~~~

This module provides the command-line interface for Localtunnel.
"""

import sys

import clint
from clint.utils import expand_path

from . import http

USAGE = '''
Usage: localtunnel [options] <localport>
    -k, --key FILE                   upload a public key for authentication
    -h, --help                       show this help
'''.lstrip()


def display_usage():
    print USAGE

def display_port_error():
    print 'Invalid port number.'


def main():
    """Main localtunnel dispatch."""

    if ('-h', '--help') in clint.args:
        display_usage()
        sys.exit()

    elif ('-k', '--key') in clint.args:

        if len(clint.args.files) != 1:
            print 'Please specify a specific public key file.'

            maybe_key = expand_path('~/.ssh/*.pub').pop(0)
            print 'Best guess: {0}\n'.format(maybe_key)
            sys.exit(1)

        keyfile = clint.args.files.pop(0)

        with open(keyfile, 'rb') as f:
            http.register_key(f.read())

        print 'Key successfully registered.'
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