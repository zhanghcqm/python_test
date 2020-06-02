import random
#打开文件
f=open(r'F:\py\123.txt','r')
#读取文件信息，赋予一个变量
data=f.read()
#关闭文件
f.close()
print('数据:',data)
print('\n')
#data是一个字符串，我们以‘，’分隔成一个列表
s=data.split(',')
#随机排序
random.shuffle(s)
print(s)