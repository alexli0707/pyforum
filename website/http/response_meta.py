#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'walker_lee'


from werkzeug.wrappers import Response
from flask import json

"""返回Response中的meta信息"""

class ResponseMeta(Exception):

    def __init__(self, code=None, description=None, http_code=400, **kwargs):
        Exception.__init__(self)
        self.http_code = http_code
        self.code = code
        self.description = description
        self.extra = kwargs

    def update(self, **kwargs):
        self.extra.update(kwargs)

    def present(self):
        data = {}
        if self.code:
            data['code'] = self.code
        if self.description:
            data['message'] = self.description

        data.update(self.extra)

        return data

    def get_response(self):
        meta = self.present()
        if meta:
            body = json.dumps({'meta': self.present()})
        else:
            body = None

        return Response(body, self.http_code, [('Content-Type', 'application/json')])

    def __call__(self, environ, start_response):
        response = self.get_response()
        return response(environ, start_response)