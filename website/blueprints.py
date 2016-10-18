#!/usr/bin/env python
# -*- coding: utf-8 -*-
from website.http.response_meta import ResponseMeta

__author__ = 'walker_lee'
from flask import Blueprint,session
import random, string
import time
"""
初始化蓝图
"""

backend = Blueprint('backend', __name__, static_folder='static', static_url_path='/admin',
                    template_folder='templates')


def _init_template_filter(app):
    def datetime_filter(n, format='%Y-%m-%d %H:%M'):
        """
        时间戳日期格式化为可读字符串
        """
        arr = time.localtime(n)
        return time.strftime(format, arr)
    app.add_app_template_filter(datetime_filter, 'datetime')

def _init_template_global(app):
    @app.app_template_global()
    def csrf_token():
        if '_csrf_token' not in session:
            session['_csrf_token'] = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        return session['_csrf_token']


def init_backend(app,server):
    """
    :param app : Flask instance
    """
    from website.controlers.backend.init_backend import init as _init_backend
    _init_backend(blueprint=backend)
    _init_template_filter(backend)
    _init_template_global(backend)
    app.register_blueprint(backend, url_prefix=app.config["ADMIN_URL_PREFIX"])
    _config_error_handler(app, server.name)



def _config_error_handler(app, blueprint_name):
    def http_error_handler(err):
        return ResponseMeta(http_code=err.code, description=err.description).get_response()

    def response_meta_handler(response_meta):
        return response_meta.get_response()

    app.error_handler_spec[blueprint_name] = {}
    for error in list(range(400, 420)) + list(range(500, 506)):
        app.error_handler_spec[blueprint_name][error] = http_error_handler
        app._register_error_handler(blueprint_name, ResponseMeta, response_meta_handler)