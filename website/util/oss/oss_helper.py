#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'walker_lee'
from abc import ABCMeta,abstractmethod

"""oss工具包"""

class OssHelper(object):
    __metaclass__ = ABCMeta
    bucket_name =None
    accessKeyId =None
    accessKeySecret = None
    endpoint = None
    imgEndpoint = None

    def __init__(self,bucket_name):
        self.bucket_name = bucket_name


    @abstractmethod
    def upload(self,src_name,stream):
        pass

    @abstractmethod
    def exist(self,src_name):
        pass

    @abstractmethod
    def get_url(self, src_name):
        pass

    @abstractmethod
    def get_img_url(self, src_name,thumbnail=''):
        pass