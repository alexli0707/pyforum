#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from website.http.main_exception import MainException

__author__ = 'walker_lee'
from flask import request, Markup, render_template, g, session, url_for

ur"""初始化后台"""


def init(app):
    init_context_processor(app)
    init_url_rules(app)
    init_before_request(app)
    init_globals(app)


def init_globals(app):
    pass


def init_before_request(app):
    @app.before_request
    def csrf_protect():
        """
        POST,PUT,DELETE请求需要带csrf_token
        """
        if request.method in ['POST', 'PUT', 'DELETE'] and request.path != url_for('.login'):
            token = session.get('_csrf_token', None)
            if not token or token != request.headers.get('csrf-token'):
                raise MainException.CSRF_TOKEN_INVALID

    @app.before_request
    def try_login():
        if not hasattr(g, 'user'):
            g.user = session.get('user', {})


def init_url_rules(app):
    # app.add_url_rule('/images', view_func=images_upload)
    # app.add_url_rule('/upload_image', view_func=images_upload)
    # app.add_url_rule('/urlimages', view_func=images_upload_by_url)
    # app.add_url_rule('/uploadClient', view_func=clients_upload)
    pass


def init_context_processor(app):
    ur"""定义html模板方法"""
    @app.context_processor
    def pjax_processor():
        """
        pjax处理器
        """

        def get_template(base, pjax=None):
            pjax = pjax or 'pjax.html'
            if 'X-PJAX' in request.headers:
                return pjax
            else:
                return base

        return dict(pjax=get_template)

    @app.context_processor
    def pagination_processor():
        """
        分页处理器
        """

        def pagination(url, pager, template=None, params={}):
            template = template or 'common/pagination.html'
            pager._dict['current'] = (pager.offset + pager.limit - 1) // pager.limit
            pager._dict['total_page'] = (pager.rows_found + pager.limit - 1) // pager.limit
            prev_offset = pager.offset - 2 * pager.limit
            pager._dict['prev_offset'] = prev_offset if prev_offset >= 0 else 0
            pager._dict['params'] = params
            pager._dict['url'] = url
            return Markup(render_template(template, data=pager))

        return dict(pagination=pagination)

    @app.context_processor
    def column_order_processor():
        """
        获取排序字段的css
        """

        def column_order(column, order, active):
            column = 'sorttable-column-%s' % column
            if active:
                order = 'sorttable-sorted-reverse' if order == 'desc' else 'sorttable-sorted'
                return '%s %s' % (column, order)
            else:
                return column

        return dict(column_order=column_order)

    @app.context_processor
    def try_active_processor():
        """
        尝试激活导航栏项目
        """

        def try_active(page_type):
            if g.page_type == page_type:
                return 'curr'
            else:
                return ''

        return dict(try_active=try_active)

    @app.context_processor
    def if_else_processor():
        """
        gives t if condition evaluates to True, and f if it evaluates to False
        """

        def if_else(condition, t, f):
            return t if condition else f

        return dict(ifelse=if_else)

    @app.context_processor
    def present_processor():
        u"""
        present enum to it's name
        eg:
            >> present(1, {1: 'Android', 2: 'iOS'}
            Android
            >> present(2, {1: 'Android', 2: 'iOS'}
            iOs
        """

        def present(enum, dict):
            return dict.get(enum, enum)

        return dict(present=present)

    @app.context_processor
    def hostname_processor():
        """
        get hostname of url
        ex: http://ng.d.cn/xianbian2/news/detail_402586_1.html => ng.d.cn
        """

        def hostname(url):
            from urlparse import urlparse
            return urlparse(url).netloc

        return dict(hostname=hostname)

    @app.context_processor
    def utility_processor():
        def permission(per):
            if g.user.get('permission') == []:
                return True
            if per in g.user.get('permission'):
                return True
            return False

        return dict(permission=permission)

    @app.context_processor
    def utility_processor():
        """激活左边栏当前模块样式"""

        def active_cur_menu(per):
            if g.uri_path.startswith(per):
                return True

            return False

        return dict(active_cur_menu=active_cur_menu)