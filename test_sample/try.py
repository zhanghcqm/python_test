a=input("请输入：")
try:
    a=int(a)
except Exception:
    print('字符串包含非数字，异常!')
else:
    print(a)
