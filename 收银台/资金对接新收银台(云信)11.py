#coding:utf-8
'''
ADVANCE-提前；
NORMAL-正常；
OVERDUE-逾期；
'''

import requests
import time
import json
import random
import var

print(var.timestamp)
url = 'http://cashierbe.dev.bkjk.cn/cashierbe/testOsg1'
#测试e9
Authorization ='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiYXJjaGltb25kZSJdLCJ1c2VyX25hbWUiOiJtZXJjaGFudC5hZG1pbkBia2prLXRlc3QuY29tIiwic2NvcGUiOlsiY3VzdG9kaWFuLnJlYWQiLCJjdXN0b2RpYW4ud3JpdGUiLCJhZHZpc2UucmVhZCIsImFkdmlzZS53cml0ZSIsImNoYW5uZWwucmVhZCIsImNoYW5uZWwud3JpdGUiLCJtZXJjaGFudC5yZWFkIiwibWVyY2hhbnQud3JpdGUiLCJwYXltZW50LnJlYWQiLCJwYXltZW50LndyaXRlIiwiY2xlYXJpbmcucmVhZCIsImNsZWFyaW5nLndyaXRlIiwicmVjb25jaWxpYXRpb24ucmVhZCIsInJlY29uY2lsaWF0aW9uLndyaXRlIiwib3JkZXIucmVhZCIsIm9yZGVyLndyaXRlIl0sImV4cCI6MzY4MjM1MDg5MSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9NRVJDSEFOVF9BRE1JTiJdLCJqdGkiOiJmYmQwNmQ1NS0yN2ViLTQ5MGQtODkxYS03NThhYjBhYzRmZmQiLCJjbGllbnRfaWQiOiJzaW11bGF0b3ItdGVzdCJ9.KqLR2IWzIwVdA2ZbxQFQlfbv2yDZI6o_UawgTUBE-KA'
#租赁测试8f
# Authorization ='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiYXJjaGltb25kZSJdLCJ1c2VyX25hbWUiOiJtZXJjaGFudC5hZG1pbkBia2prLmNvbSIsInNjb3BlIjpbImN1c3RvZGlhbi5yZWFkIiwiY3VzdG9kaWFuLndyaXRlIiwiYWR2aXNlLnJlYWQiLCJhZHZpc2Uud3JpdGUiLCJjaGFubmVsLnJlYWQiLCJjaGFubmVsLndyaXRlIiwibWVyY2hhbnQucmVhZCIsIm1lcmNoYW50LndyaXRlIiwicGF5bWVudC5yZWFkIiwicGF5bWVudC53cml0ZSIsImNsZWFyaW5nLnJlYWQiLCJjbGVhcmluZy53cml0ZSIsInJlY29uY2lsaWF0aW9uLnJlYWQiLCJyZWNvbmNpbGlhdGlvbi53cml0ZSIsIm9yZGVyLnJlYWQiLCJvcmRlci53cml0ZSJdLCJleHAiOjM2NzMyNTI5MTMsImF1dGhvcml0aWVzIjpbIlJPTEVfTUVSQ0hBTlRfQURNSU4iXSwianRpIjoiYWY1MzQ0MWYtMTVhYS00NmU4LWIwMzktN2Y0MGNlZTllNWEzIiwiY2xpZW50X2lkIjoic2ltdWxhdG9yIn0.yZmCQz_jumD0JzIC0TQ1Snnw2AzrRJnM-Sln65Cy6hg'

headers ={"Authorization":Authorization,"Content-Type":"application/json","sys-source":"CASHIER"}
data ={"userInfo":{"phone":"13717734812","partnerKey":"ZXFQ","userName":"朱峰","userId":"5c80d483ed9445069aa0e23a4e2296bf","idNo":"110103198809090618"},"merchantId":"e990ebd3-b56f-4b44-abfc-e4f54d6cf657","tradeNum":"QRHK154175960212084091100111","callBackUrlArray":[{"name":"callbackUrl","url":"http://declorder.test.bkjk.cn/decoloan-web/repayment/callback"},{"name":"pageReturnUrl","url":"https://mt.test.bkjk.com/front-decoration/repay-confirm?id=1654690&from=record&code=15416753356436"},{"name":"cancelPageUrl","url":"https://mt.test.bkjk.com/front-decoration/repay-confirm?id=1654690&from=record&code=15416753356436"}],"payInfo":{"amount":"1239.44","tradeDesc":"交易成功"},"repayInfo":{"period":"3","financeNo":"15416753356436","loanNo":"FP15416756127286","providerCode":"ZJF103","payeeCode":"39","type":"NORMAL","amountDetails":[{"amount":1111.11,"type":"PRINCIPAL"},{"amount":128.33,"type":"INTEREST"},{"amount":0.00,"type":"FINE"}],"periodNo":"code:15416753356436#periods:3"}}

s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)
print(t['data'])
