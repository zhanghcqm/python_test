#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/5/27 13:54
# @Author: zhc
import pytest

#不带参数是默认scope=“function”

# @pytest.fixture(scope="module")
# def login():
#     print('输入账号、密码，登录')

def test_s1(login):
    print("case1:登陆后玩一下")

def test_s2():
    print("case1:不用登陆，玩一下")

def test_s3(login):
    print("case3:登陆后看一下")


if __name__ == '__main__':
    pytest.main("-s",'test_fix.py')

