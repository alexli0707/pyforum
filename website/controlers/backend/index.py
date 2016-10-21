#!/usr/bin/env python
# -*- coding: utf-8 -*-
from website.http.main_exception import MainException
from ...blueprints import backend
from flask import render_template

__author__ = 'walker_lee'



@backend.route('/')
def index():
    # return render_template('backend/test.html')
    return render_template('backend/test_pjax.html')



