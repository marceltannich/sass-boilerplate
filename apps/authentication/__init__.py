# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - Marcel Tannich
"""

from flask import Blueprint

blueprint = Blueprint(
    'authentication_blueprint',
    __name__,
    url_prefix=''
)
