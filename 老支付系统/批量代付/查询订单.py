'''
查询订单
https://payment.test.bkjk.com/api/df/queryOrder
'''
#coding:utf-8
import request
import json
import random
import time

url = 'https://payment.test.bkjk.com/api/df/queryOrder'
data = {"outReqNo":"10006201811090023"}

t1 = request.request(url, data)
# print(t1)

js = json.dumps(t1, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print('返回报文格式化:')
print(js)

s1 = json.loads(t1['data'])
js11 = json.dumps(s1, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print('返回data格式化:')
print(js11)