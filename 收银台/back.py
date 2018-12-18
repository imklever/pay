#coding:utf-8

import requests
import time
import json
import random
import var
# import to

url = 'http://dev-ewallet-api.ehomepay.com.cn/ewallet/cashier/remPay'
headers ={"Content-Type":"application/json","X-BK-UUSSSO-Token":var.XBKUUSSSOToken}
data ={
	"rembId": "xxx01",
	# "rembId": to.rembId,
	"merchantNo":"T201801221000002"
}

s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)


