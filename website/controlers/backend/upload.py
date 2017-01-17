#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask.ext.login import login_required

from website.blueprints import backend
from website.controlers.wrap_func import confirm_required
from website.http.request import Request
from website.http.response import Response
from website.helper.oss_helper import  upload_image as oss_upload_image

__author__ = 'walker_lee'



@backend.route('/upload/image',methods=['POST','PUT'])
@login_required
@confirm_required
def upload_image():
    """目前上传图片采用ckeditor中drop and paste file的方式进行数据交换"""
    return oss_upload_image()

