'''
创建协议接口
https://payment.test.bkjk.com/api/protocol/create
'''
#coding:utf-8
import request
import json
import random
import time


print('####################创建协议开始##################')
##创建协议入参
data1 = {"transDesc":"test1","businessId":"1","channelType":"LFT","cashierType":"ONLINEBANK"}
#创建协议请求地址
url1 = 'https://payment.test.bkjk.com/api/protocol/create'

t1 = request.request(url1, data1)

sss1 = json.loads(t1)
ss11 = sss1['data']
ss1 = json.loads(ss11)
transNo = ss1['transNo']
print('------')
print('接口状态：'+sss1['msg'])
print('transNo:'+transNo,'amount:'+ss1['amount'],'onpassageAmount:'+ss1['onpassageAmount'],'outAmount:'+ss1['outAmount'],'cashierType:'+ss1['cashierType'])
print('------')

print('####################创建协议结束##################')

print(len(sss1.keys()))
print(sss1.keys())
print(len(ss1.keys()))
print(ss1.keys())
