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
url2 = '/houseapi/ebankOrderList'

url = url1+url2

headers ={"Content-Type":"application/json"}
data = {
    "customerName":"",                   #客户姓名
    "customerCardNo":"",                 #银行卡号
    "refundBankCard":"",                  #卡号
    "beginTransferAccountsDate":"",       #申请时间左边界
    "endTransferAccountsDate":"",         #申请时间右边界
    "status":""                             #审核状态【WAIT_AUDIT：待审核  PASS: 通过  REJECT:拒绝】
}
s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)