#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/5/27 10:55
# @Author: zhc

import pytest

def func(x):
    return x +1
def test_answer ():
    assert func(3)

def f():
    #解释器请求退出
    raise SystemExit()

def test1():
    with pytest.raises(SystemExit):
        f()
if __name__ == '__main__':
    pytest.main('-v','test_sample.py')