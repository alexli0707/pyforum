#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

import config

__author__ = 'walker_lee'

try:
    from raven.contrib.flask import Sentry

except ImportError:
    pass


class SentryHelper(object):
    @staticmethod
    def init_app(app):
        if hasattr(config, 'SENTRY_DSN'):
            sentry = Sentry()
            sentry.init_app(app, dsn=config.SENTRY_DSN, logging=True, level=logging.ERROR)
        return app

