i=0
while i<3:
 score = float(input('please enter a num:'))
 if score>=0 and score <=100:
    if score > 80:
        print('您的分数是：%s'%score,'优秀')
    elif score > 60:
        print('您的分数是：%s'%score,'及格')
    elif score > 0:
        print('您的分数是：%s'%score,'不及格')
 else:
    print('您输入的数值不合法')
 i=i+1
if i==3:
    print('输入次数过多，请稍后再试！')