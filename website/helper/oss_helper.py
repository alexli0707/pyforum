#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import requests
from flask import request
from flask import url_for

from config import IMAGE_BUCKET
from website.commons.singleton import Singleton
from website.http.main_exception import MainException
from website.http.response import Response
from website.models.photo import Photo

__author__ = 'walker_lee'
"""对象存储工具"""

class LocalOss(metaclass=Singleton):
    image_bucket =IMAGE_BUCKET

    def __init__(self):
        self.image_uri = url_for('.static','imgs/'+IMAGE_BUCKET)
        pass

    @staticmethod
    def oss():
        return LocalOss()


    def upload_image(self,media_src, stream):
        if isinstance(stream, str) and os.path.exists(stream):
            stream = open(stream, 'rb')
        else:
            stream.seek(0)
        # 上传到oss
        res = self.bucket.put_object(media_src, stream)
        print (res)

        if res.status / 100 == 2:
            return True

        return False

    def exist_image(self,media_src):
        """判断文件是否存在"""
        res = requests.head(self._uri + self._get_object(media_src))
        if res.status_code == 404:
            return None
        else:
            return res.headers

    def _get_object(self, media_src):
        return (media_src + '@' + self.thumbnail) if self.thumbnail else media_src





def upload_image():
    """对应处理上传图片采用ckeditor中drop and paste file的方式进行数据交换
        http://docs.ckeditor.com/#!/guide/dev_file_upload
    """
    upload_file = request.files.get('upload')
    if not upload_file:
        raise MainException.NO_FILE_DATA
        # return Response({
        #     'uploaded': 0,
        #     'error': {
        #         "message": "未找到上传文件"
        #     }
        # })
    else:
        photo  =Photo()
        if photo.add(upload_file):
            pass
        return Response({})