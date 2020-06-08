i=0
while i<3:
    score = float(input('please enter a num:'))
    if 0 <= score <= 100:
        if score > 80:
            print('您的分数是：%s'% score,'优秀')
        elif score > 60:
            print('您的分数是：%s'% score,'及格')
        elif score >= 0:
            print('您的分数是：%s'% score,'不及格')
    else:
        print('请输入0-100的数字！')
    i=i+1
if i==3:
    print('您的输入次数已达限制，请稍后输入！')