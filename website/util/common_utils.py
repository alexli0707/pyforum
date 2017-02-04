#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'walker_lee'


from config import APP_MODE

def is_dev_mode():
    """是否开发环境"""
    if APP_MODE == 'DEV':
        return True
    return False

def filter_same_element(to_filter_list):
    return list(set(to_filter_list))

