# -*- coding: utf-8 -*-

import requests

from .packages.omnijson import loads as from_json
from .packages.omnijson import JSONError


LOCALTUNNEL_API = 'http://open.localtunnel.com/'

def open_localtunnel():
    """Requests a new connection to localtunnel."""
    r = requests.get(LOCALTUNNEL_API)

    try:
        return from_json(r.content)
    except JSONError, why:
        raise why

print open_localtunnel()