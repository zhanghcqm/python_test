#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020/5/28 9:56
# @Author: zhc


"""
函数式：调用 _thread 模块中的start_new_thread()函数来产生新线程。语法如下:
_thread.start_new_thread ( function, args[, kwargs] )
参数说明:
function - 线程函数。
args - 传递给线程函数的参数,他必须是个tuple类型。
kwargs - 可选参数。
"""

import _thread,time

#为线程定义一个函数
def print_time(threadName,delay):
    count=0
    while count < 5:
        time.sleep(delay)
        count+=1
        print("%s: %s" % (threadName, time.ctime(time.time())))

#创建两个线程
try:
    _thread.start_new_thread(print_time,("Thread-1",1))
    _thread.start_new_thread(print_time,("Thread-2",3))
except:
    print("Error: 无法启动线程")

while 1:
    pass