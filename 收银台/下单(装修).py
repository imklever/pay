#coding:utf-8

import requests
import time
import json
import random
import var

print(var.timestamp)
url = 'http://cashierbe.dev.bkjk.cn/cashierbe/testOsg1'
Authorization ='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiYXJjaGltb25kZSJdLCJ1c2VyX25hbWUiOiJtZXJjaGFudC5hZG1pbkBia2prLXRlc3QuY29tIiwic2NvcGUiOlsiY3VzdG9kaWFuLnJlYWQiLCJjdXN0b2RpYW4ud3JpdGUiLCJhZHZpc2UucmVhZCIsImFkdmlzZS53cml0ZSIsImNoYW5uZWwucmVhZCIsImNoYW5uZWwud3JpdGUiLCJtZXJjaGFudC5yZWFkIiwibWVyY2hhbnQud3JpdGUiLCJwYXltZW50LnJlYWQiLCJwYXltZW50LndyaXRlIiwiY2xlYXJpbmcucmVhZCIsImNsZWFyaW5nLndyaXRlIiwicmVjb25jaWxpYXRpb24ucmVhZCIsInJlY29uY2lsaWF0aW9uLndyaXRlIiwib3JkZXIucmVhZCIsIm9yZGVyLndyaXRlIl0sImV4cCI6MzY4MjM1MDg5MSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9NRVJDSEFOVF9BRE1JTiJdLCJqdGkiOiJmYmQwNmQ1NS0yN2ViLTQ5MGQtODkxYS03NThhYjBhYzRmZmQiLCJjbGllbnRfaWQiOiJzaW11bGF0b3ItdGVzdCJ9.KqLR2IWzIwVdA2ZbxQFQlfbv2yDZI6o_UawgTUBE-KA'
headers ={"Authorization":Authorization,"Content-Type":"application/json","sys-source":"CASHIER"}
data ={"userInfo":{"phone":"18710896696","partnerKey":"ZXFQ","userName":"犯花痴","userId":"955886def69f4a3b95a6b629b1e54e9a","idNo":"612724199010062017"},"merchantId":"e990ebd3-b56f-4b44-abfc-e4f54d6cf657","tradeNum":var.timestamp,"callBackUrlArray":[{"name":"callbackUrl","url":"http://declorder.test.bkjk.cn/decoloan-web/repayment/callback"},{"name":"pageReturnUrl","url":"https://mt.test.bkjk.com/front-decoration/repay-confirm?id=891129&from=record&code=15402025159200"},{"name":"cancelPageUrl","url":"https://mt.test.bkjk.com/front-decoration/repay-confirm?id=891129&from=record&code=15402025159200"}],"payInfo":{"amount":"355.66","tradeDesc":"交易成功"},"repayInfo":{"period":"5","financeNo":"15402025159200","loanNo":"FP15402025323935","payeeCode":"34","type":"NORMAL","amountDetails":[{"amount":333.33,"type":"PRINCIPAL"},{"amount":22.33,"type":"INTEREST"},{"amount":0.00,"type":"FINE"}],"periodNo":"code:15402025159200#periods:5"}}

s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)
print(t['data'])

