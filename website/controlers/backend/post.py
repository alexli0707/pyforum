#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_paginate import Pagination, get_page_args
from playhouse.flask_utils import object_list

from website.http.paginate import FlaskPagination
from website.http.request import Request
from website.http.response import Response
from website.models.post import Post, PostTag

__author__ = 'walker_lee'

from flask_login import login_required

from website.controlers.backend.wrap_func import check_permission
from website.controlers.wrap_func import confirm_required
from flask import render_template, g
from ...blueprints import backend


@backend.route('/posts')
@login_required
@confirm_required
@check_permission
def post_list():
    rows = Post.select()
    return object_list('post/post/list.html', paginate=FlaskPagination(query=rows), query=rows,
                       context_variable='rows', paginate_by=10, check_bounds=False, page_header={
            'title': '文章列表',
        })

@backend.route('/posts/create')
@login_required
@confirm_required
@check_permission
def create_post_page():
    return render_template('post/post/post.html', check_bounds=False, page_header={
            'title': '创建文章',
        })


@backend.route('/posts',methods=['POST'])
@login_required
@confirm_required
@check_permission
def create_post():
    data = Request(request).json()
    print(data)
    return Response()



@backend.route('/tags')
@login_required
@confirm_required
@check_permission
def post_tag_list():
    rows = PostTag.select()
    return object_list('post/tag/list.html', paginate=FlaskPagination(query=rows), query=rows,
                       context_variable='rows', paginate_by=10, check_bounds=False,  page_header={
            'title': '标签列表',
        })

