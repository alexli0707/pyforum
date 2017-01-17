#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'walker_lee'

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonDemo(metaclass=Singleton):
    pass

if __name__ == '__main__':
    singleton_a = SingletonDemo()
    singleton_b = SingletonDemo()
    assert id(singleton_a) == id(singleton_b)