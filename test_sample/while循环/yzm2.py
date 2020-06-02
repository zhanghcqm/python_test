import random
import string
s = 0
while True:
    name = input('账号： ')
    pwd = input('密码： ')
    if s <= 2:
        if name == 'admin' and pwd == '123':
            print('登录成功！')
            break
        else:
            print('登录失败！')
            s += 1
    else:
        v_code = ''.join(random.sample(string.digits + string.ascii_letters, 4))
        v = input('验证码 | %s |：' % v_code)
        if name == 'admin' and pwd == '123' and v.lower() == v_code.lower():
            print('登录成功！')
            break
        else:
            print('登录失败！')

