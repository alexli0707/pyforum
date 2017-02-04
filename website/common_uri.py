#!/usr/bin/env python
# -*- coding: utf-8 -*-
from website.models.photo import Photo

__author__ = 'walker_lee'



def images_download(photo_src):
    info = photo_src.split('@')
    if len(info) > 1:
        photo_src, thumbnail = info
    else:
        photo_src, thumbnail = photo_src, None

    photo_obj = Photo()
    return photo_obj.output(photo_src, thumbnail)

# images_download.__permission__ = 'download_images'

images_download.methods = ['GET']