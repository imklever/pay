#coding:utf-8
import request
import json
import random
import time


print('####################创建协议开始##################')
##创建协议入参
data1 = {"transDesc":"test1","businessId":"2","channelType":"LFT"}
#创建协议请求地址
url1 = 'http://172.29.66.21:80/api/protocol/create'

t1 = request.request(url1, data1)

sss1 = json.loads(t1)
ss11 = sss1['data']
ss1 = json.loads(ss11)
transNo = ss1['transNo']
print('transNo:'+transNo,'amount:'+ss1['amount'],'onpassageAmount:'+ss1['onpassageAmount'],'outAmount:'+ss1['outAmount'])

print('####################创建协议结束##################')

print(len(sss1.keys()))
print(sss1.keys())
print(len(ss1.keys()))
print(ss1.keys())
