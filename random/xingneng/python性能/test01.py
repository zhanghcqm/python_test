import requests

def adduser():
    for i in range(1,51):
        adddata={
            'billing.firstName': ('t0%d'% i),
            'billing.lastName': 'tt',
            'billing.country': 'CN',
            'billing.stateProvince': 'sichuan',
            'emailAddress': ('1234567%d@qq.com' % i),
            'userName': ('1234567%d@qq.com' % i),
            'password': '123456',
            'checkPassword': '123456',
        }
        requests.post('http://192.168.1.241:8080/shop/customer/register.html',data=adddata)
adduser()
