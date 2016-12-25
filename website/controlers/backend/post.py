#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_paginate import Pagination, get_page_args

from website.http.paginate import CustomPagination
from website.models.post import Post

__author__ = 'walker_lee'

from flask_login import login_required

from website.controlers.backend.wrap_func import check_permission
from website.controlers.wrap_func import confirm_required
from flask import render_template,g
from ...blueprints import backend

@backend.route('/posts')
@login_required
@confirm_required
@check_permission
def post_list():
    page = CustomPagination.get_page()
    rows = Post.select().paginate(page=page,paginate_by=10)
    pagination = CustomPagination(rows = rows,page=page)
    return render_template('backend/post/list.html',rows= rows,pagination =pagination)