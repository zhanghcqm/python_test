#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/5/27 14:16
# @Author: zhc
import pytest

@pytest.mark.parametrize('x',[0,1])
@pytest.mark.parametrize('y',[2,3])

def test_foo(x,y):
    print("测试数据组合：x->%s,y->%s"%(x,y))


if __name__ == '__main__':
    pytest.main('-s','test_canshu2.py')
