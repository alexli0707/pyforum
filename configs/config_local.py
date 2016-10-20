#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'walker_lee'


# 端口配置
API_PORT = 15102
ADMIN_PORT = 15103

# Blueprint配置
WWW_URL_PREFIX = '/www'
ADMIN_URL_PREFIX = '/admin'
M_URL_PREFIX = '/m'

# 服务器地址
M_ADDRESS = 'http://localhost:5000/m/'
API_ADDRESS = 'http://localhost:5000/v2/api'

SUPER_ADMIN = ('admin', 'admin')

# 数据库配置
MYSQL_NG = ('172.25.1.111', 3306, 'unitest_forum', 'unitest_forum', 'unitest_forum', True, 'utf8')
MYSQL_GC = ('172.25.1.111', 3306, 'ngds_user', 'ngds_user.mysql', 'game_store', True, 'utf8')
MYSQL = MYSQL_NG

OBJECT_ID_WIDTH = 10 ** 13  # 全局ID的长度

# 日志配置
# LOG_SILENT = True
LOG_SILENT = False

# 图片管理
IMAGEURL = 'http://127.0.0.1:5000/v2/images'
IMAGE_BUCKET = 'nb-imgs'
UPLOAD_TMP_DIR = '/tmp'

# 阿里云oss配置
OSS_ACCESS_KEY_ID = 'hNW2QKIROxHlqbDG'
OSS_ACCESS_KEY_SECRET = 'UHxy2kEJX1D0C4onYcOjfBK22Ky7j9'
OSS_END_POINT = 'http://oss-cn-hangzhou.aliyuncs.com'
OSS_IMG_END_POINT = 'http://img-cn-hangzhou.aliyuncs.com'  # 图片访问域名, 用于处理图片缩放等

TEMPLATES_AUTO_RELOAD =True #自动刷新html



# SESSION
SESSION_SALT = 'h\xf2\x80-\x93\x80\x9d\x8b\xdf_\t\xa4>5\xa2w\x91\xcd\xe1\x82\xdb\xde\x18\xfe'


# app 环境模式,目前分为DEV 与PRO(线上)
APP_MODE = 'DEV'
