'''
创建协议接口
https://payment.test.bkjk.com/api/protocol/create
'''
#coding:utf-8
import requests
import json
import random
import time

url= 'http://morder.test.bkjk.cn/morder/refund-request/list'


headers ={"Content-Type":"application/json"}
# data = {"pageNum": 1, "pageSize": 10}
data = {}
s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)