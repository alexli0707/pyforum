#!/usr/bin/env python
# -*- coding: utf-8 -*-
from website.app import db

__author__ = 'walker_lee'

from peewee import IntegerField, CharField, PrimaryKeyField, Model, TextField


class Post(Model):
    id = PrimaryKeyField()
    title = CharField()
    user_id = IntegerField()
    summary = TextField()
    content = TextField()
    created_at = IntegerField()
    updated_at = IntegerField()
    posted_at = IntegerField()
    read_count = IntegerField()
    like_count = IntegerField()
    comment_floor = IntegerField()

    class Meta:
        database = db
        db_table = 'post'
