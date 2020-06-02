"""
99乘法表
"""
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s'%(j,i,i*j),end=' ')
#     print()

"""
冒泡排序
"""
# List=[2,4,6,22,34,21,5,52,1,8]
# for i in range (len(List)-1):
#     for j in range (len(List)-1):
#         if List[j]>List[j+1]:
#            List[j],List[j+1] = List[j+1],List[j]
# print(List)

"""
1,2,3,4能组成多少个互不相同且无重复数字的三位数？分别是什么？
"""

List=[1,2,3,4]
sum=0
for i in range (len(List)):
    for j in range (len(List)):
        for k in range (len(List)):
                if List[i] != List[j] and List[i]!= List[k] and List[j] != List[k]:
                    print(100*List[i]+10*List[j]+List[k])
                    sum+=1
print('总共{}个这种数字'.format(sum))

"""
输出直角三角形
"""
#方法一：
# for i in range (1,6):
#     for j in range (i):
#         print('*',end='')
#     print()
#方法二：
# for i in range(6):
#     print("*"*i)

"""
输出等边三角形
"""
#方法一：
# for i in range(1,6):
#     for j in range(6-i):
#         print(' ',end='')
#     for k in range(i):
#         print('* ',end='')
#     print('')
#方法二：
# for i in range(1,6):
#     for j in range(6-i):
#         print(' ',end='')
#     print('* '*i)