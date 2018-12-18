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
url2 = '/houseapi/ebankOrderAudit'

url = url1+url2

headers ={"Content-Type":"application/json"}
data = {
    "refundRequestId":"",           #退费申请ID
    "auditDate":"",                 #财务操作时间
    "status":"",                    #审核状态 【PASS :通过，REJECT:拒绝】
    "note":""                       #财务备注
}
s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)