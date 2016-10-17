#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

__author__ = 'walker_lee'
ur"""应用初始化入口以及配置"""




def create_app(config=None, server_name=None):
    ur"""初始化flask相关配置"""
    app = Flask()
    app.config.from_object(config)
    init_blueprint(app,server_name)


def init_blueprint(app, server_name):
    # if 'backend' == server_name or 'all' == server_name:
    pass
