#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/5/27 11:50
# @Author: zhc
import pytest
#函数式用例方式


def setup_module():
    print("setup_module:整个.py模块只执行一次，比如所有用例开始前只打开一次浏览器")

def teardown_module():
    print("teardown_module:整个.py模块只执行一次，比如所有用例结束后只最后关闭浏览器")

def setup_function():
    print("setup_fuc:每个用例开始前都会执行")

def teardown_function():
    print("setup_fuc:每个用例结束后都会执行")


def test_one(login):
    print('正在执行---test_one')
    x='this'
    assert 'h' in x

def test_two():
    print('正在执行---test_two')
    x='hello'
    assert hasattr(x,'check')

def test_three():
    print('正在执行---test_three')
    a='hello'
    b='hello,world'

    assert a in b

if __name__ == '__main__':
    pytest.main('-s','test_fixt.py')