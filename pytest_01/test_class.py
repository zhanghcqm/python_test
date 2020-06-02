#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/5/27 11:33
# @Author: zhc

import pytest
class TestClass:
    def test_one(self):
        x='this'
        assert 'h' in x

    @pytest.mark.skipif(3>2,reason='跳过测试，条件成立')
    def test_two(self):
        x='hello'
        assert hasattr(x,'check')

    @pytest.mark.skip(reason='no way currentlg testing this')
    def test_four(self):
        x='hello'
        assert hasattr(x,'check')

    def test_three(self):
        x='this'
        assert 'h' in x

if __name__ == '__main__':
    pytest.main(['-q test_class'])