#!/usr/bin/env python
# -*- coding: utf-8 -*-
from website.http.response_meta import ResponseMeta

__author__ = 'walker_lee'
from flask import Blueprint,session,render_template
import random, string
import time
from website.constant import SESSION_CSRF_TOKEN
"""
初始化蓝图
"""

backend = Blueprint('backend', __name__, static_folder='static', static_url_path='',
                    template_folder='templates/backend')


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
        if SESSION_CSRF_TOKEN not in session:
            session[SESSION_CSRF_TOKEN] = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        return session[SESSION_CSRF_TOKEN]

def init_backend(app,server):
    """
    :param app : Flask instance
    """
    from website.controlers.backend.init_backend import init as _init_backend
    _init_backend(blueprint=backend)
    _init_template_filter(backend)
    _init_template_global(backend)
    _config__backend_error_handler(backend, server.name)
    app.register_blueprint(backend, url_prefix=app.config["ADMIN_URL_PREFIX"])



def _config__backend_error_handler(blueprint, blueprint_name):
    """
    后台异常如果是4XX异常则返回对应页面,5XX异常则返回对应服务端异常页面
    :param blueprint:
    :param blueprint_name:
    :return:
    """
    @blueprint.errorhandler(500)
    def internal_server_error(e):
        return render_template('backend/error/500.html')

    #由于是后台,不用处理未捕捉异常,直接抛出来便于发现处理
    # @blueprint.errorhandler(Exception)
    # def error(e):
    #     return render_template('backend/error/500.html')

    @blueprint.errorhandler(ResponseMeta)
    def handler_response_meta(response_meta):
        return response_meta.get_response()