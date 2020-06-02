#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/5/27 11:45
# @Author: zhc
import pytest
class TestClass:
    def test_one(self):
        x='this'
        assert 'h' in x

    def test_two(self):
        x='hello'
        assert hasattr(x,'check')


    def test_three(self):
        x='this'
        assert 'h' in x

if __name__ == '__main__':
    pytest.main(['-q test_class'])