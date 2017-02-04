# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# import os
#
# import oss2
# from enum import Enum
#
# from config import OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET, OSS_END_POINT, OSS_IMG_END_POINT
# from website.utils.oss.oss_helper import OssHelper
#
# __author__ = 'walker_lee'
#
#
# class AliBucketEnum(Enum):
#     img = 'nb-imgs'
#     pkg = 'oss-newgamer-com/ng-pkgs'
#
#
# class AliOssHelper(OssHelper):
#     ur"""目前将阿里云的bucket分为两种,一类是阿里云提供处理图片方案的图片oss,另一类可归并为pkgoss"""
#     def __init__(self, bucket_name):
#         super(AliOssHelper, self).__init__(bucket_name)
#         self.accessKeyId = OSS_ACCESS_KEY_ID
#         self.accessKeySecret = OSS_ACCESS_KEY_SECRET
#         self.endpoint = OSS_END_POINT
#         auth = oss2.Auth(self.accessKeyId, self.accessKeySecret)
#         if bucket_name == AliBucketEnum.img.value:
#             self.imgEndpoint = OSS_IMG_END_POINT
#             self.bucket = oss2.Bucket(auth, self.endpoint, bucket_name)
#             self._uri = "{}/{}/".format(self.endpoint, bucket_name)
#             self._img_uri = "{}/{}/".format(self.imgEndpoint, bucket_name)
#         elif bucket_name == AliBucketEnum.pkg.value:
#             self.bucket = oss2.Bucket(auth, self.endpoint, bucket_name)
#             self._uri = "{}/{}/".format(self.endpoint, bucket_name)
#
#
#     def upload(self, src_name, stream):
#         if isinstance(stream, str) and os.path.exists(stream):
#             stream = open(stream, 'rb')
#         else:
#             stream.seek(0)
#
#             # 上传到oss
#         res = self.bucket.put_object(src_name, stream)
#         print res
#
#         if res.status / 100 == 2:
#             return True
#
#         return False
#
#
#     def exist(self, src_name):
#         return self.bucket.object_exists(src_name)
#
#     def get_url(self, src_name):
#         return self._uri + src_name
#
#     def get_img_url(self, src_name, thumbnail=''):
#         return self._img_uri + ((src_name + '@' + thumbnail) if thumbnail else src_name)
