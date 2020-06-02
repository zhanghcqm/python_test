import requests
import json

url = "https://cvd-test.xiaoduoai.com/v1/vobot_admin/frontend_call/entp_list"

querystring={
    "unit_id": 238,
    "begin_ts": 1539964800,
    "end_ts": 1542556799,
    "result": 0
}
#qs = json.dumps(querystring)
headers={
    "authorization": "2142 cceb09b4"
}
response = requests.request("post", url, headers=headers, data=json.dumps(querystring))
#response = requests.request("get", url, headers=headers, params=querystring)
data = response.json()["error_code"]
try:
    assert (0 == data)
except Exception as error:
    print("请检查状态码")

print(response.json())