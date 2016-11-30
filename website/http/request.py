#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import json
from website.http.response_meta import ResponseMeta

__author__ = 'walker_lee'

class Request(object):
    def __init__(self, request):
        self.request = request
        self.raw = self.request.data
        self._json_body = None

    def json(self, raw_str=None):
        if self._json_body is not None:
            return self._json_body

        if raw_str is not None:
            self.raw = raw_str

        try:
            self._json_body = json.loads(self.raw)
            return self._json_body
        except:
            raise ResponseMeta(http_code=406)