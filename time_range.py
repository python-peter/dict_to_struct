#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: time_range.py
@time: 2017/7/15 13:54
"""

import time
from contextlib import contextmanager

@contextmanager
def timeblock(label):
    print 'start'
    start = time.time()
    try:
        yield
    finally:
        print 'end'
        end = time.time()
        print '{}: {}'.format(label, end - start)

def fun():
    a = 0
    for i in range(100):
        a += i
    print a

with timeblock(1):
    fun()


