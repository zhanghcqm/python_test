#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/5/27 14:00
# @Author: zhc

import pytest

@pytest.fixture()

def login():
    print("输入账号、密码，登录")