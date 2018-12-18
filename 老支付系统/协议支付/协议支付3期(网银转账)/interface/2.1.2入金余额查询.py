'''
入金接口
https://payment.test.bkjk.com/api/protocol/prepay
'''
#coding:utf-8
import json
import random
import time
import random


import request

transNo = 'TR181212162943269771115'

data3 = transNo

url3 = 'https://payment.test.bkjk-inc.com/api/protocol/queryprotocolbalance'

t3 = request.request1(url3, data3)

sss3 = json.loads(t3)
ss31 = sss3['data']
ss3 = json.loads(ss31)
# print(sss3)
# print(ss3)
# print(ss31)
print(sss3['data'])
print('可用余额：'+ss3['data']['balance'])