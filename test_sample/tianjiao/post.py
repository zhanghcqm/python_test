import requests
import json

url="http://192.168.1.241:8080/shop/customer/logon.html"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
    "Accept":"application/json, text/javascript, */*; q=0.01"
}
questring={
    "userName":"123456@qq.com",
    "password":"123456",
    "storeCode":"DEFAULT"
}
res=requests.post(url,headers=headers,data=json.dumps(questring))

print(res.status_code)
assert res.json()['response']['status'] == 0 ,"response is wrong"

# try:
#     assert (-1==res.json()['response']['status'])
# except Exception as error:
#     print('error')
