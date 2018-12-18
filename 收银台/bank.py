#coding:utf-8

import requests
import time
import json
import random
import var

Authorization ='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiYXJjaGltb25kZSJdLCJ1c2VyX25hbWUiOiJtZXJjaGFudC5hZG1pbkBia2prLmNvbSIsInNjb3BlIjpbImN1c3RvZGlhbi5yZWFkIiwiY3VzdG9kaWFuLndyaXRlIiwiYWR2aXNlLnJlYWQiLCJhZHZpc2Uud3JpdGUiLCJjaGFubmVsLnJlYWQiLCJjaGFubmVsLndyaXRlIiwibWVyY2hhbnQucmVhZCIsIm1lcmNoYW50LndyaXRlIiwicGF5bWVudC5yZWFkIiwicGF5bWVudC53cml0ZSIsImNsZWFyaW5nLnJlYWQiLCJjbGVhcmluZy53cml0ZSIsInJlY29uY2lsaWF0aW9uLnJlYWQiLCJyZWNvbmNpbGlhdGlvbi53cml0ZSIsIm9yZGVyLnJlYWQiLCJvcmRlci53cml0ZSJdLCJleHAiOjM2NzMyNTI5MTMsImF1dGhvcml0aWVzIjpbIlJPTEVfTUVSQ0hBTlRfQURNSU4iXSwianRpIjoiYWY1MzQ0MWYtMTVhYS00NmU4LWIwMzktN2Y0MGNlZTllNWEzIiwiY2xpZW50X2lkIjoic2ltdWxhdG9yIn0.yZmCQz_jumD0JzIC0TQ1Snnw2AzrRJnM-Sln65Cy6hg'
num = '8fa029c4-6b87-4a84-ab3a-a0b8a9dc9229'
url1 = 'http://archimonde.dev.bkjk.cn/archimonde/api/bank-limit-settings/'
url2 = '/supported-banks'
url = url1 + num + url2
# print(url)
headers ={"Authorization":Authorization,"Content-Type":"application/json","X-BK-UUSSSO-Token":var.XBKUUSSSOToken}
data = {"paymentCategory":"FASTPAY","transactionType":"TOP_UP","bankAccountType":"PRIVATE","limitCreditCard":"false"}

s = requests.get(url,params=data,headers=headers)
# print(s.status_code)
print(s.url)
t = s.json()

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
        print(t1[i]['bankName'])
except:
    print("不支持信用卡")

# print("+++++++++++++++++++++++++++")
#
# js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
# print(js)

