#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading

from website.util.oss.local_oss_helper import LocalOssHelper

__author__ = 'walker_lee'


oss_buckets={}

def oss_by_bucket_name(bucket_name):
    if not oss_buckets.get(bucket_name):
        mutex = threading.Lock()
        # 锁定
        mutex.acquire(1)
        if not oss_buckets.get(bucket_name):
            oss_buckets[bucket_name] = LocalOssHelper(bucket_name)
        mutex.release()
    return oss_buckets[bucket_name]


