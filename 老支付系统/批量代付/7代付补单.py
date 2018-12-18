#coding:utf-8

'''
代付补单
https://payment.test.bkjk.com/dfapi/updateorder
'''
#coding:utf-8
import requests
import json
import random
import time

url = 'https://payment.test.bkjk.com/dfapi/updateorder'
headers ={"Content-Type":"application/json"}
data ={"payOrderNo":"TR181112200356446969102"}

s = requests.post(url,data=json.dumps(data),headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)

