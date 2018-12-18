'''
创建协议接口
https://payment.test.bkjk.com/api/protocol/create
'''
#coding:utf-8
import requests
import json
import random
import time

url1 = 'https://payment.test.bkjk.com'
url2 = '/ebankapi/refundOrder'

url = url1+url2

headers ={"Content-Type":"application/json"}
data = {
    "bankFlowNo":"9745086303680168",            #转账银行流水号
    "userName": "11",         #当前用户登录名
    "uid": "20262772",           #当前用户登录id
    "remark": "111"            #remark
}
s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)