#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ...blueprints import backend

__author__ = 'walker_lee'


print('init index')

@backend.route('/')
def index():
    return 'Hello Py'



