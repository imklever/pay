'''
创建协议接口
https://payment.test.bkjk.com/api/protocol/create
'''
#coding:utf-8
import request
import json
import random
import time

url1 = 'https://payment.test.bkjk.com'
url2 = '/ebankapi/selectRepairOrder'

url = url1+url2

headers ={"Content-Type":"application/json"}
data = {
    "refundNo":""            #退款流水号
}
s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)