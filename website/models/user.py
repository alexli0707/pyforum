#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import current_app
from flask.ext.login import AnonymousUserMixin, UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from peewee import Model, IntegerField, CharField
from website.app import db, login_manager
from werkzeug.security import check_password_hash


class User(UserMixin, Model):

    id = IntegerField(primary_key=True)
    email = CharField()
    username = CharField()
    password_hash = CharField()
    confirmed = IntegerField


    class Meta:
        database = db
        db_table = 'users'


    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def generate_confirmation_token(self, expiration=3600):
        """生成验证邮箱的token"""
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        """验证邮箱"""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        # 验证成功,写入数据库
        self.confirmed = True
        self.save()
        return True

    def generate_reset_token(self, expiration=3600):
        """生成重置密码的token"""
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        """重置密码"""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        # 验证成功,写入数据库
        self.password = new_password
        self.save()
        return True

    def __repr__(self):
        return '<User %r>' % self.username

"""
匿名用户
"""
class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.get(User.id == int(user_id))

