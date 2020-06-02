user=input('请输入用户名:')
passwd=int(input('请输入密码：'))
a=open(r"F:\py\1.txt",'r')
u=a.read()
print(u)
p=u.splitlines()
print(p)
for i in range(len(p)):
   d=p[i].split(' ')
   print(d)
   if user==d[0] and passwd==int(d[1]):
           print('登录成功')
           break
else:
       print('登录失败')