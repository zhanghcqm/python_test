#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/5/27 14:31
# @Author: zhc

"""
pytest里面用 xfail 标记用例为失败的用例，可以直接跳过。
 把登录写为前置操作
 对登录的账户和密码参数化，参数用 data = [{"user":"amdin","psw":"111"}]表示
 多个用例放到一个 Test_xx 的 class 里
 test_01，test_02， test_03 全部调用 fixture 里面的 login 功能
 test_01 测试登录用例
 test_02 和test_03 执行前用 if 判断登录的结果，登录失败就执行，pytest.xfail("登录不成功, 标记为 xfail")
"""

import pytest

data=[{'user':'admin','psw':''}]

@pytest.fixture(scope="module")
def login(request):
    user=request.param['user']
    psw=request.param['psw']
    print("正在操作登录，账号： %s, 密码： %s" % (user, psw))
    if psw:
        return True
    else:
        return False

@pytest.mark.parametrize("login", data, indirect=True)
class Test_xx():
    def test_01(self,login):
        """
        用例1登录
        :param login:
        :return:
        """
        result=login
        print("用例1：{}".format(result))
        assert result == True

    def test_02(self,login):
        """
        用例2
        :param login:
        :return:
        """
        result=login
        print("用例2，登录结果：{}".format(result))
        if not result:
            pytest.xfail("登录不成功，标记为xfail")

        assert 1 == 1

    def test_03(self, login):
        """
        用例3
        :param login:
        :return:
        """
        result = login
        print("用例3，登录结果：{}".format(result))
        if not result:
            pytest.xfail("登录不成功，标记为xfail")

        assert 1 == 1


if __name__ == '__main__':
    pytest.main('-s','test_xfail.py')
