#coding:utf-8

'''
代付绑卡
https://payment.test.bkjk.com
URL：/dfapi/querybankcnaps
'''
#coding:utf-8
import requests
import json
import random
import time

url = 'https://payment.test.bkjk.com/dfapi/querybankcnaps'
headers ={"Content-Type":"application/json"}
data = {
    "bankNameKeyWord":"工商银行",
    "appId":"10007"
}

s = requests.post(url, data=json.dumps(data), headers=headers)
t = s.json()
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)


