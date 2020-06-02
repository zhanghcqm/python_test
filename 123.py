#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/4/28 9:02
# @Author: zhc

# list = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
# s1=0
# s2=0
# for i in list:
#     if i > 0:
#         s1 += 1
#     elif i < 0:
#         s2 += 1
# print(s1,s2)
# b = [i for i in list if i > 0]
# print("大于 0 的个数：%s" % len(b))

"""
打印出 100-999 所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数
字立方和等于该数本身。例如：153 是一个"水仙花数"，因为 153=1 的三次方＋
5 的三次方＋3 的三次方。
"""
# for i in range(100,1000):
#     s=str(i)
#     sum = 0
#     for j in s:
#         sum+=int(j)**len(s)
#     if sum ==i:
#         print(i)

"""
如果一个数恰好等于它的因子之和，则称该数为“完全数”，又称完美数或完备
数。 例如：第一个完全数是 6，它有约数 1、2、3、6，除去它本身 6 外，其余
3 个数相加，
1+2+3=6。第二个完全数是 28，它有约数 1、2、4、7、14、28，除去它本身 28
外，其余 5 个数相加，1+2+4+7+14=28。
那么问题来了，求 1000 以内的完全数有哪些？"""

# for i in range(0,1000):
#     s = 0
#     for j in range(1,i):
#         if i%j==0:
#             s+=j
#     if s==i:
#         print(i)
#
# l = [2, 4, 3, 9, 7, 5, 1, 8, 6]
# for i in range(len(l)-1):
#     for j in range(0,len(l)-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1] = l[j+1],l[j]
#
# print(l)
"""
写一个小程序：控制台输入邮箱地址（格式为 username@companyname.com），
程序识别用户名和公司名后，将用户名和公司名输出到控制台。
要求：
1. 校验输入内容是否符合规范（xx@yy.com）, 如是进入下一步，如否则抛出提
示"incorrect email format"。注意必须以.com 结尾
2. 可以循环“输入--输出判断结果”这整个过程
3. 按字母 Q（不区分大小写）退出循环，结束程序"""
#
# while True:
#     email = str(input("请输入您的邮箱地址："))
#     if email[-4:] == '.com':
#         print("邮箱地址正确：{}".format(email))
#     else:
#         print("邮箱地址错误，请重新输入！")

list=[1,2,3,4]
# for i in range(1,100):
#     l.append(i)
# print(l[::2])

# it=iter(l)
# for i in it:
#     print(i,'\n')

import sys


# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()


# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
# g = foo()
# print(next(g))
# print("*"*20)
# print(next(g))

# import os,re
# dir=os.path.dirname('python')
# print(os.getcwd())
#




"""
python多线程
"""
# import _thread
# import time
#
# def print_time(threadName ,delay):
#     count=0
#     while count<5:
#         time.sleep(delay)
#         count+=1
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#
#
# try:
#     _thread.start_new_thread(print_time,("thread-1",2))
#     _thread.start_new_thread(print_time,("thread-2",2))
# except:
#     print("error:无法启动线程")
#
# while 1:
#     pass

import pymysql

db=pymysql.connect("localhost","root","123456","test")
cursor=db.cursor()

sql="select * from grade"
try:
    cursor.execute(sql)
    db.commit()
    results=cursor.fetchall()
    print(results)

except:
    db.rollback()
db.close()

# def gen_random_string(str_len):
#     """
#     随机获取字符串
#     :param str_len: 输入需要几位的字符串
#     :return:
#     """
#     random_char = string.digits+string.ascii_letters
#     gen_char=random.sample(random_char,str_len)
#
#     gen_random_str=''.join(gen_char)
#     return gen_random_str


























