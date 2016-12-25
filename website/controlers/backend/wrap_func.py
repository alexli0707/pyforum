#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps

from flask import request,g

from website.models.module import ManageModule, RoleModule
from flask_login import current_user

__author__ = 'walker_lee'


def check_permission(f):
    """
    后台初始化路由并进行权限检查
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        init_menus()
        return f(*args, **kwargs)

    return decorated_function




def init_menus():
    g.uri_path = request.path
    menus,submenus = ManageModule.get_menus_and_submenus()
    g.menu = menus
    parent_id = 0
    for menu in submenus:
        if request.path.startswith(menu['prefix']):
            parent_id = menu['parent_id']
    g.sub_menu = submenus
    g.cur_menu = [row for row in submenus if row['parent_id'] == parent_id]
    g.modules = RoleModule.get_modules_by_role_id(role_id=current_user.role_id)
