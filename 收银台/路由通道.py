#coding:utf-8
'''
云信绑还款卡路由
ALLINPAY 通联 CFCAPAY 中金
'''

import requests
import time
import json
import random
import var
import re

#测试账号e99
Authorization ='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiYXJjaGltb25kZSJdLCJ1c2VyX25hbWUiOiJtZXJjaGFudC5hZG1pbkBia2prLXRlc3QuY29tIiwic2NvcGUiOlsiY3VzdG9kaWFuLnJlYWQiLCJjdXN0b2RpYW4ud3JpdGUiLCJhZHZpc2UucmVhZCIsImFkdmlzZS53cml0ZSIsImNoYW5uZWwucmVhZCIsImNoYW5uZWwud3JpdGUiLCJtZXJjaGFudC5yZWFkIiwibWVyY2hhbnQud3JpdGUiLCJwYXltZW50LnJlYWQiLCJwYXltZW50LndyaXRlIiwiY2xlYXJpbmcucmVhZCIsImNsZWFyaW5nLndyaXRlIiwicmVjb25jaWxpYXRpb24ucmVhZCIsInJlY29uY2lsaWF0aW9uLndyaXRlIiwib3JkZXIucmVhZCIsIm9yZGVyLndyaXRlIl0sImV4cCI6MzY4MjM1MDg5MSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9NRVJDSEFOVF9BRE1JTiJdLCJqdGkiOiJmYmQwNmQ1NS0yN2ViLTQ5MGQtODkxYS03NThhYjBhYzRmZmQiLCJjbGllbnRfaWQiOiJzaW11bGF0b3ItdGVzdCJ9.KqLR2IWzIwVdA2ZbxQFQlfbv2yDZI6o_UawgTUBE-KA'

url = 'http://archimonde.dev.bkjk.cn/archimonde/api/advises/selected-payment?paymentCategory=FASTPAY&transactionType=CHARGE&bankAccountType=PRIVATE&requestedAmount=101&bankAcronym=CCB&bankAccountNo=6226095711989751&merchantId=e990ebd3-b56f-4b44-abfc-e4f54d6cf657&enableTrace=true&bankCardType=DEBIT_CARD'
print(url)
headers ={"Authorization":Authorization,"Content-Type":"application/json"}

s = requests.get(url,headers=headers)
print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)

try:
    if t['code'] == 'BR1100':
        print('没有可用通道')
    if t['code'] == 'BR2000':
        print('可用通道：'+t['content']['sections'][0]['paymentType'])
except:
    pass