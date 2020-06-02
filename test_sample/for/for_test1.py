#！/usr/bin/python3.7
# -*- coding: utf-8 -*-
#@Time   :2020/4/6 16:10
#@Author :zhc
"""
range(a,m,k):n 初始值，m 结束值，k 步长默认为1，会生成初始值为你，结束值为m-1，递减或者是递增的整数序列
range(n):默认生成一个0到n-1的整数序列
"""
# for i in range (6,0,-1):
#     print(i)
#
# print(list(range(-1,5)))

# s=0
# for i in range (1,5):
#     print('第{}次输入!'.format(i))
#     sex=input('please enter your sex:')
#     if sex == 'f':
#         age=int(input('please enter your age:'))
#         if age >= 10 and age <= 12:
#             print('恭喜你加入足球队！')
#             s=s+1
#         else:
#             print('年龄不符合要求')
#     else:
#         print('性别不符合要求')
# print('总共有%s名队员可以加入足球队！'%(s))
sum1=0
sum2=0
for item in range (0,101):
    if item %2 ==0:
        sum1+=item
    else:
        sum2+=item
print("0-100之间的所有偶数和为%s,奇数和为%s" % (sum1,sum2))