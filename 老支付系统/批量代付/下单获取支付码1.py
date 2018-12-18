'''
下单获取支付码
https://payment.test.bkjk.com/api/df/pay
'''
#coding:utf-8
import request
import json
import random
import time

url = 'https://payment.test.bkjk.com/api/df/pay'
data = {
    "businessId":"6",
    "outReqNo": "10006201811130002",
    "amount": "611.11",
    # "amount": "100.00",
    "notifyUrl": "www.baidu.com",
    "bindCardIds":["181113180430298144145"],
    "merchantInfoList":[
        {
            "recAccountId":"EHP1010001003311",
            "recAccountName":"大连链家房地产经纪有限公司",
            "recAmt":"200.00",
            "recMerchantNo":"23456"
        },
        {
            "recAccountId": "EHP1010000014846",
            "recAccountName": "欧阳希",
            "recAmt": "100.00",
            "recMerchantNo": "2345678"
        },
        {
            "recAccountId": "EHP1010000009437",
            "recAccountName": "理房通环球帝国支付公司",
            "recAmt": "311.11",
            "recMerchantNo": "3456789"
        }
    ]}




t1 = request.request(url, data)
# print(t1)

js = json.dumps(t1, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print('返回报文格式化:')
print(js)

s1 = json.loads(t1['data'])
js11 = json.dumps(s1, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print('返回data格式化:')
print(js11)