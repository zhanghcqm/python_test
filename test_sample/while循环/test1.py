#1-10相加
# i=0
# s=0
# while i<=10:
#     s+=i
#     i+=1
# print(s)


i=1
s=0
while i<=10:
    print('第{}次输入：'.format(i))
    sex=input('please enter your sex:')
    if sex == 'f':
        age=int(input('please enter your age:'))
        if age >= 10 and age <= 12:
            print('恭喜你加入足球队！')
            s=s+1
        else:
            print('年龄不符合要求')
    else:
        print('性别不符合要求')
    i+=1
print(s)
