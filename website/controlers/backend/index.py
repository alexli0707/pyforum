#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'walker_lee'

from ...blueprints import backend


@backend.route('/')
def index():
    return 'Hello Py'
