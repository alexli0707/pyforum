#!/usr/bin/env python
# -*- coding: utf-8 -*-
from playhouse.shortcuts import model_to_dict

from website.app import db_wrapper
from peewee import IntegerField, CharField, PrimaryKeyField, Model, SmallIntegerField, ForeignKeyField

__author__ = 'walker_lee'


class ManageModule(db_wrapper.Model):
    id = PrimaryKeyField()
    parent_id = IntegerField()
    name = CharField()
    uri = CharField()
    prefix = CharField()
    weight = SmallIntegerField()

    class Meta:
        db_table = 'manage_module'

    @staticmethod
    def get_menus_and_submenus():
        """获取菜单与子菜单"""
        rows = [model_to_dict(row) for row in
                ManageModule.select().order_by(ManageModule.parent_id.asc(), ManageModule.weight.desc())]
        menus = [row for row in rows if row['parent_id'] == 0]
        submenus = [row for row in rows if row['parent_id'] != 0]
        return menus, submenus


class RoleModule(db_wrapper.Model):
    id = PrimaryKeyField()
    role_id = SmallIntegerField()
    module_id = IntegerField()

    # module_id = ForeignKeyField(ManageModule)


    class Meta:
        db_table = 'role_module'

    @staticmethod
    def get_modules_by_role_id(role_id):
        module_ids = [row.module_id for row in RoleModule.select().where(RoleModule.role_id == role_id)]
        return module_ids
