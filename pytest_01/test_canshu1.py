#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/5/27 14:08
# @Author: zhc
import pytest

@pytest.mark.parametrize('test_input,expected',
                         [('3+5',8),("2+4",6),
                          pytest.param("4*7",43,marks=pytest.mark.xfail)])

def test_eval(test_input,expected):
    assert eval(test_input) == expected


if __name__ == '__main__':
    pytest.mian('-s','test_canshu1.py')
