#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'walker_lee'


"""
约定:在flask框架中g,session中有用到存储作用的键名都统一放在constant.py中便于管理以及代码阅读,根据存放的容器指定KEY的prefix
"""

SESSION_CSRF_TOKEN = '_csrf_token'