#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'walker_lee'
from flask import Blueprint,session
import random, string
import time


admin = Blueprint('admin', __name__, static_folder='static', static_url_path='/admin', template_folder='templates')

def init_template_filter(app):
    def datetime_filter(n, format='%Y-%m-%d %H:%M'):
        """
        时间戳日期格式化为可读字符串
        """
        arr = time.localtime(n)
        return time.strftime(format, arr)
    app.add_app_template_filter(datetime_filter, 'datetime')

def init_template_global(app):
    @app.app_template_global()
    def csrf_token():
        if '_csrf_token' not in session:
            session['_csrf_token'] = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        return session['_csrf_token']