#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask.ext.paginate import Pagination

__author__ = 'walker_lee'


class CustomPagination(Pagination):
    """封装自定义分页,peewee与flask-pagination结合,默认分页10条数据,可以在传入per_page中调整"""

    def __init__(self, rows, found=0, **kwargs):
        per_page = kwargs.get('per_page', 10)
        css_framework = kwargs.get('css_framework', 'bootstrap3')
        total = kwargs.get('total', rows.count())
        record_name = kwargs.get('record_name', 'rows')
        kwargs['per_page'] = per_page
        kwargs['css_framework'] = css_framework
        kwargs['total'] = total
        kwargs['record_name'] = record_name
        kwargs['show_single_page'] = True
        super().__init__(found=found, **kwargs)

    @staticmethod
    def get_page():
        return request.args.get('page', type=int, default=1)

