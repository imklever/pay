#coding:utf-8

import requests
import time
import json
import random

# print(var.XBKUUSSSOToken)
# print(var.timestamp)
url = 'http://api.test.bkjk.cn/uus/user/auth'
headers ={"Content-Type":"application/json"}
data ={
    "accountName": "13142691734",
    "accountType": "PHONE",
    "authType": "CODE",
    "clientId": "bkjk-0823",
    "clientSecret": "MrQx28VIOfCtFQXjf4teDqQFMntrjjEp",
    "deviceInfo": {
        "appIP": "",
        "appMAC": "",
 "appVersion": "280",
        "channel": "BKJK",
        "deviceFingerPrint": "",
        "deviceId": "865132034031752",
        "os": "",
        "osVersion": "",
        "source": ""
    },
 "grantType": "password",
    "inviteCode": "",
    "inviteType": "",
    "partnerKey": "BKJK",
    "partnerUID": "",
    "password": "666666",
    "verifyToken": ""
}

s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
# print(js)
token = t['content']['access_token']
print(token)