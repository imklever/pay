#coding:utf-8

import requests
import time
import json
import random
import var
import re
import tk


merchantId = '8fa029c4-6b87-4a84-ab3a-a0b8a9dc9229'
url1 = 'http://api.dev.bkjk.cn/cashierbe/bank-limit-settings/getSupportBankList/'
url = url1 + merchantId
print(url)
headers ={"X-BK-UUSSSO-Token":tk.token,"Content-Type":"application/json","Accept":"application/json"}

s = requests.get(url, headers=headers)
print(s.status_code)
t = s.json()
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)

print("+++++++++++++++++++++++++++")

t1 = t['content']['DEBIT_CARD']
print("支持的借记卡银行总数%d，银行列表：" %len(t1))
for i in range(len(t1)):
    print(t1[i]['bankName'])

print("+++++++++++++++++++++++++++")

try:
    t2 = t['content']['CREDIT_CARD']
    print("支持的信用卡银行总数%d，银行列表：" %len(t2))
    for i in range(len(t2)):
        print(t2[i]['bankName'])
except:
    print("不支持信用卡")