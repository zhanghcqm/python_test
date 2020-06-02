#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/5/27 12:02
# @Author: zhc
"""
setup/teardown 和 unittest 里面的 setup/teardown 是一样的
功能，setup_class 和 teardown_class 等价于 unittest 里面的
setupClass 和 teardownClass
"""
import pytest
#类和方法

class TestCase:

    def setup(self):
        print("setup: 每个用例开始前执行")

    def teardown(self):
        print("teardown: 每个用例结束后执行")

    def setup_class(self):
        print("setup_class ：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class ：所有用例执行之后")

    def setup_method(self):
        print("setup_method: 每个用例开始前执行")

    def teardown_method(self):
        print("teardown_method: 每个用例结束后执行")

    def test_one(self):
        print('正在执行---test_one')
        x='this'
        assert 'h' in x

    def test_two(self):
        print('正在执行---test_two')
        x='hello'
        assert hasattr(x,'check')

    def test_three(self):
        print('正在执行---test_three')
        a='hello'
        b='hello,world'

        assert a in b

if __name__ == '__main__':
    pytest.main('-s','test_fixt')