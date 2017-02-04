#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from flask import url_for

from config import APP_STATIC
from website.util.oss.oss_helper import OssHelper
import requests

__author__ = 'walker_lee'


class LocalOssHelper(OssHelper):
    def __init__(self, bucket_name):
        super().__init__(bucket_name)

    def upload(self, src_name, stream):
        if isinstance(stream, str) and os.path.exists(stream):
            stream = open(stream, 'rb')
        else:
            stream.seek(0)
        stream.save(self._get_img_path(src_name))
        if self.exist(src_name):
            return True
        else:
            return False

    def exist(self, src_name):
        img_path = self._get_img_path(src_name)
        return os.path.exists(img_path)

    def _get_img_path(self, src_name):
        return APP_STATIC + self.bucket_name + '/' + src_name

    def get_url(self, src_name):
        pass

    def get_img_url(self, src_name, thumbnail=''):
        return url_for('.static', filename=self.bucket_name + '/' + src_name)
