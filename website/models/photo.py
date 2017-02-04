#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import io
import pickle

import time

from werkzeug.utils import redirect

from config import IMAGE_BUCKET
from website.app import db
from website.http.main_exception import MainException
from website.util.oss import oss_manager

__author__ = 'walker_lee'
from peewee import IntegerField, CharField, PrimaryKeyField, Model, TextField, SmallIntegerField, BlobField
from PIL import Image, ExifTags


IMAGES_ALLOWED = ('gif', 'jpeg', 'png', 'bmp', 'webp')

class Photo(Model):
    id = PrimaryKeyField()
    filename = CharField()
    src = CharField()
    format = CharField()
    width = SmallIntegerField()
    height = SmallIntegerField()
    created_at = IntegerField(default=time.time())
    meta = BlobField()

    class Meta:
        database = db
        db_table = 'photo'

    @staticmethod
    def oss():
        return oss_manager.oss_by_bucket_name(IMAGE_BUCKET)


    def add(self,upload_img):
        string_types = (type(''), type(u''))
        if type(upload_img) in (string_types) and ('http://' in upload_img or 'https://' in upload_img):
            ret = self.try_down_url(upload_img)
            if ret:
                self.filename = upload_img
                upload_img = ret
            else:
                return False
        self._extract_image(upload_img)
        #此处需要判断,如果本地数据库已经存在该图片,则不进行创建
        self.save()
        storage_path = self.storage_path(self.src)
        # 文件已存在，直接返回成功
        if self.oss().exist(storage_path):
            return True
        # 文件不存在，保存文件
        if self.oss().upload(storage_path, upload_img):
            return True

        return False

    def try_down_url(self, url):
        import requests
        r = requests.get(url)
        if r.status_code == 200:
            return io.StringIO(r.content)
        else:
            return None

    def set_src(self, upload_file):
        if not self.src and self.format:
            upload_file.seek(0)
            h = hashlib.md5(upload_file.read()).hexdigest()
            self.src = "{}.{}".format(h, self.format)

    def _extract_image(self, upload_file):
        if not self.filename:
            self.filename = getattr(upload_file, 'filename', None)

        if isinstance(upload_file, Image.Image):
            image = upload_file
        else:
            image = Image.open(upload_file)
        self.format = image.format.lower()
        if self.format not in IMAGES_ALLOWED:
            raise MainException.PHOTO_FORMAT_FORBIDDEN

        self.width, self.height = image.size
        self.set_src(upload_file)

        self.meta = self.extract_meta(image)

    @staticmethod
    def storage_path(src):
        return src

    @staticmethod
    def extract_meta(image):
        exif = None
        if hasattr(image, '_getexif'):
            exif = image._getexif()

        if not exif:
            return None

        meta = {}
        for k, v in exif.items():
            if k in ExifTags.TAGS:
                key = ExifTags.TAGS[k]
                if key == 'GPSInfo':
                    v = {ExifTags.GPSTAGS[gk]: gv for gk, gv in v.items() if gk in ExifTags.GPSTAGS}

                try:
                    meta[key] = v
                except:
                    return None

        return pickle.dumps(meta)

    def output(self, photo_src, thumbnail=None):
        """输出图片"""
        storage_path = self.storage_path(photo_src)

        if thumbnail is None:
            return redirect(self.oss().get_img_url(storage_path))

        # 获取缩略图大小
        tmp = thumbnail.split('.')
        if len(tmp) == 2:
            thumbnail = tmp[0]

        if thumbnail not in self._thumbnail:
            raise MainException.PHOTO_THUMB_MODE_INVALID

        # return redirect(self.oss(object_prefix=thumbnail).get_img_url(storage_path))
        return redirect(self.oss().get_img_url(storage_path,thumbnail))


