#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_login import login_required
from website.controlers.wrap_func import confirm_required
from website.http.main_exception import MainException
from ...blueprints import backend
from flask import render_template

__author__ = 'walker_lee'


@backend.route('/')
@login_required
@confirm_required
def index():
    return render_template('backend/template.html')
