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
    "businessId":"12",
    "outReqNo": "10006201811120089",
    "amount": "6811.11",
    # "amount": "100.00",
    "notifyUrl": "www.baidu.com",
    "bindCardIds":["181112200330671971101"],
    "merchantInfoList":[
        {
            "recAccountId":"EHP2010000000215",
            "recAccountName":"vZZd56OaerhiEs0VcpRTww==",
            "recAmt":"100.00",
            "recMerchantNo":"12345"
        },
        {
            "recAccountId":"EHP1010001003311",
            "recAccountName":"大连链家房地产经纪有限公司",
            "recAmt":"200.00",
            "recMerchantNo":"23456"
        },
        {
            "recAccountId":"EHP2010000000213",
            "recAccountName":"vZZd56OaerhiEs0VcpRTww==",
            "recAmt":"300.00",
            "recMerchantNo":"34567"
        },
        {
            "recAccountId": "EHP2010000000211",
            "recAccountName": "hutt_test3",
            "recAmt": "400.00",
            "recMerchantNo": "45678"
        },
        {
            "recAccountId": "EHP2010000000209",
            "recAccountName": "hutt_test2",
            "recAmt": "500.00",
            "recMerchantNo": "56789"
        },
        {
            "recAccountId": "EHP2010000000127",
            "recAccountName": "hutt_test1001378",
            "recAmt": "600.00",
            "recMerchantNo": "67890"
        },
        {
            "recAccountId": "EHP1010000021147",
            "recAccountName": "wolfking",
            "recAmt": "700.00",
            "recMerchantNo": "78901"
        },
        {
            "recAccountId": "EHP1010000021145",
            "recAccountName": "hutt",
            "recAmt": "800.00",
            "recMerchantNo": "89012"
        },
        {
            "recAccountId": "EHP1010000021124",
            "recAccountName": "demo",
            "recAmt": "900.00",
            "recMerchantNo": "90123"
        },
        {
            "recAccountId": "EHP1010000014846",
            "recAccountName": "欧阳希",
            "recAmt": "1100.00",
            "recMerchantNo": "2345678"
        },
        {
            "recAccountId": "EHP1010000009437",
            "recAccountName": "理房通环球帝国支付公司",
            "recAmt": "1211.11",
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