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
url2 = '/ebankapi/manualProcessingList'

url = url1+url2

headers ={"Content-Type":"application/json"}
data = {
    "bankAccNum":"6222020200020589358",            #银行卡号
    "inStatus": "",             #处理状态	待人工处理退款 '0' 已处理 '1'
    "refundStatus": "",         #退款状态 ("0", "未退款"),("1", "退款中"),("2", "退款成功"),("3", "退款失败");
    "bankFlowNo": "",           #转账银行流水号
    "startTime": "",            #起始日期
    "endTime": ""                #结束日期
}
s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)