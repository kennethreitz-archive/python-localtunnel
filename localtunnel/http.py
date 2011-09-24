# -*- coding: utf-8 -*-

"""
localtunnel.http
~~~~~~~~~~~~~~~~

This module provides
"""

import requests

from .packages.omnijson import loads as from_json
from .packages.omnijson import JSONError


LOCALTUNNEL_API = 'http://open.localtunnel.com/'


def register_key(pub_key):
    """Publishes a public key to the localtunnel service."""

    r = requests.post(LOCALTUNNEL_API, data={'key': pub_key})
    r.raise_for_status()


def register_tunnel():
    """Requests a new connection to the localtunnel service."""
    r = requests.get(LOCALTUNNEL_API)

    try:
        return from_json(r.content)
    except JSONError, why:
        raise why

