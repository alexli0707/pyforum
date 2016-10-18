#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'walker_lee'
import pkgutil
# from ...utils.func import init_logger
# LOGGER = init_logger(__name__)

__path__ = pkgutil.extend_path(__path__, __name__)
for importer, modname, _ in pkgutil.walk_packages(path=__path__, prefix=__name__+'.'):
    __import__(modname)
    print("load_component:{}".format(modname))