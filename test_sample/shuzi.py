#有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
n=0
for i in range(1,5):
    for j in range(1,5):
        for z in range(1,5):
            if i!=j and j!=z and i!=z:
               s=100*i+10*j+z
               print('%d'%s)
               n=n+1
print('这样的数字有：',n)

#一些四位数,百位数字都是3,十位数字都是6,并且它们既能被2整除,又能被 3整除,
#求这样的四位数中最大的和最小的两数各是几?
l=[]
for i in range(1000,10000):
    if i%3==0 and i%2==0 and i%1000//100==3 and i%100//10==6:
        l.append(i)
print('最大的数字是:',max(l))
print('最小的数字是:',min(l))

#一张纸可以对折无限次，纸张厚度为0.07毫米。问多少次对折至少可以超过8848米？
n=0
while True:
    s = 0.07 * 2 ** n
    if s > 8848000:
        break
    else:
        n=n+1
print(s)
print(n)

#草莓15元一斤，火龙果3元一个，香蕉2元一斤，刚好花完200元，每种至少有一个/斤，有多少种可能，并列举出来
a=200//15
b=200//3
c=200//2
n=0
for i in range(1,a+1):
    for j in range(1,b+1):
        for z in range(1,c+1):
            if 15*i+3*j+2*z==200:
                n=n+1
                print('草莓',i,'火龙果',j,'香蕉',z)
print('一共%d种可能'%n)



