#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/5/27 11:33
# @Author: zhc
"""
命令行选项
-k ,使用表达式指定特定的测试用例运行,你想选择名字里包含add的测试用例，可以这么写pytest -k add
-x ,执行用例遇到失败的立即结束
--maxfail=num ,指定失败几次之后才停止，-x的选项其实就是--maxfail=1
-s ,测试运行时输出任何符合标准的输出流信息(print)
--lf ,用于重跑之前失败的用例，若没有任何失败，则全部重跑；若如上次运行的4个用例中，有2个失败了，
那么使用--lf（--last-failed）选项，则当前只会运行上次失败的那两个用例。
-v ,啰嗦模式，啥信息都显示
-q ,安静模式，只显示关键的信息（例如失败原因）
"""

import pytest
class TestClass:
    def test_one(self):
        x='this'
        assert '1' in x

    @pytest.mark.skipif(1>2,reason='跳过测试，条件成立')
    def test_two(self):
        x='hello'
        assert hasattr(x,'check')

    @pytest.mark.skip(reason='no way currentlg testing this')
    def test_four(self):
        x='hello'
        assert hasattr(x,'check')

    def test_three(self):
        x='this'
        assert '2' in x

if __name__ == '__main__':
    pytest.main('-v','test_class.py')