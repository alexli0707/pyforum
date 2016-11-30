#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'walker_lee'


from flask import g
from flask import make_response
from flask import json


class Response(object):

    def __init__(self, data=None, meta=None, pagination=None):
        """
        data 可以是：
        1、集合类型 list，tuple
        2、God
        3、Array

        God、Array 有 present() 方法用于转为 dict
        """
        result = {}

        page = None
        if pagination or isinstance(data, (list, tuple)):
            if hasattr(pagination, 'present'):
                page = pagination.present()
            elif hasattr(g, 'pagination'):
                page = g.pagination.present()
            else:
                page = None

        if page:
            result['pagination'] = page

        if hasattr(data, 'present'):
            result['data'] = data.present()
        elif isinstance(data, (list, tuple)):
            #如果是集合
            newdata = []
            for obj in data:
                if hasattr(obj, 'dump'):
                    obj = obj.dump()

                newdata.append(obj)

            result['data'] = newdata
        else:
            result['data'] = data

        if hasattr(meta, 'present'):
            result['meta'] = meta.present()

        response = make_response(json.dumps(result))
        response.headers['Content-Type'] = 'application/json'

        if hasattr(g, 'headers'):
            for k, v in g.headers.items():
                response.headers[k] = v

        self.response = response

    def __call__(self, environ, start_response):
        return self.response(environ, start_response)