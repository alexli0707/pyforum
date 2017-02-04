#!/usr/bin/env python
# -*- coding: utf-8 -*-
from website.http.response_meta import ResponseMeta

__author__ = 'walker_lee'
"""定义异常"""


class MainException(object):
    # 请求已成功，请求所希望的响应头或数据体将随此响应返回。
    OK = ResponseMeta(http_code=200)
    #请求已经被实现，而且有一个新的资源已经依据请求的需要而创建。
    CREATED = ResponseMeta(http_code=201)
    #资源已经删除。
    NO_CONTENT = ResponseMeta(http_code=204)
    #由于包含语法错误，当前请求无法被服务器理解。
    BAD_REQUEST = ResponseMeta(http_code=400)
    #当前请求需要用户验证。
    UNAUTHORIZED = ResponseMeta(http_code=401)
    #服务器已经理解请求，但是拒绝执行它。
    FORBIDDEN = ResponseMeta(http_code=403)
    #请求失败，请求所希望得到的资源未被在服务器上发现。
    NOT_FOUND = ResponseMeta(http_code=404)
    #请求行中指定的请求方法不能被用于请求相应的资源。
    METHOD_NOT_ALLOWED = ResponseMeta(http_code=405)
    #请求的资源的内容特性无法满足请求头中的条件，因而无法生成响应实体。
    NOT_ACCEPTABLE = ResponseMeta(http_code=406)
    #服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。
    INTERNAL_SERVER_ERROR = ResponseMeta(http_code=500)
    #作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。
    BAD_GATEWAY = ResponseMeta(http_code=502)
    #由于临时的服务器维护或者过载，服务器当前无法处理请求。
    SERVICE_UNAVAILABLE = ResponseMeta(http_code=503)
    #未能及时从上游服务器收到响应。
    GATEWAY_TIMEOUT = ResponseMeta(http_code=504)

    INSERT_OK = ResponseMeta(1000, '添加成功', http_code=200)
    DELETE_OK = ResponseMeta(1000, '删除成功', http_code=200)
    DELETE_FAILURE = ResponseMeta(1000, '删除失败', http_code=200)

    PLATFORM_NOT_FOUND = ResponseMeta(code=1001, description='未知平台')
    SOMANY_ARGS = ResponseMeta(code=1002, description='参数过长')
    CSRF_TOKEN_INVALID = ResponseMeta(code=1003, description='csrf token错误', http_code=403)
    DEVICE_NOT_FOUND = ResponseMeta(code=1004, description='未知设备参数')

    EMAIL_OR_PASSWORD_ERROR = ResponseMeta(code=2001,description='用户名或者密码错误')
    DUPLICATE_EMAIL = ResponseMeta(code=2002,description='邮箱已注册')
    DUPLICATE_USERNAME = ResponseMeta(code=2003,description='用户名已注册')

    PHOTO_FORMAT_FORBIDDEN = ResponseMeta(code=5001, description='不支持的图片类型')
    PHOTO_THUMB_MODE_INVALID = ResponseMeta(code=5002, description='缩略图方式未定义')
    PHOTO_OSS_GET_FAIL = ResponseMeta(code=5003, description='无法获取原图数据')

    NO_FILE_DATA = ResponseMeta(code=6001, description='上传文件数据为空')
    CHUNK_UPLOAD_MD5_ERROR = ResponseMeta(code=6002, description='校验失败')
    CHUNK_UPLOAD_ERROR = ResponseMeta(code=6003, description='上传失败')
    FILE_NOT_SUPPORT = ResponseMeta(code=6004, description='不支持的文件格式')



    ACCOUNT_NOT_FOUND = ResponseMeta(code=10001, description='用户不存在')
