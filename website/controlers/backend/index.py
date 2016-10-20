#!/usr/bin/env python
# -*- coding: utf-8 -*-
from website.http.main_exception import MainException
from ...blueprints import backend

__author__ = 'walker_lee'



@backend.route('/')
def index():
    return 'Hello Py'



