#coding:utf-8

'''
代付绑卡
https://payment.test.bkjk.com/
URL：/dfapi/pagedforder
请求参数：
{"pageSize": "10", "pageNum": "1", "payStatus": "SUCCESS", "appId": "10005",
        "outReqNo": "10005002",
        "payOrderNo": "TR180726150021251359101",
        "businessId": "1",
        "endTime":"1533200776000",
        "startTime":"1532423788000",
       "merchantName":"北京美锦互联网金融信息有限公司", 商户名称
        "bankCardNo": "6214920208512356", 银行卡号
        "amount": "600.00" }
'''
#coding:utf-8
import requests
import json
import random
import time

url = 'https://payment.test.bkjk.com/dfapi/pagedforder'
headers ={"Content-Type":"application/json"}
data = {
        "pageSize": "10",
        "pageNum": "1",
        "payStatus": "SUCCESS",
        "appId": "",
        "outReqNo": "",
        "payOrderNo": "TR181109103233103779110",
        "businessId": "",
        "endTime":"",
        "startTime":"",
       "merchantName":"",
        "bankCardNo": "",
        "amount": "" }

s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)

