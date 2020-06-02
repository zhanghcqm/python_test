import random
f=open(r'F:\py\123.txt','r')
data=f.read()
f.close()
print('人员名单:',data)
print('\n')
s=data.split(',')
#随机抽取n个
def select(n):
    print(random.sample(s,n))
select(2)
#print(random.choice(s))   随机取1个