#coding:utf-8

import requests
import time
import json
import random
import var

print(var.timestamp)
url = 'http://uldaman.dev.bkjk.cn/api/orders'
Authorization ='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiYXJjaGltb25kZSJdLCJ1c2VyX25hbWUiOiJtZXJjaGFudC5hZG1pbkBia2prLWNyZWQuY29tIiwic2NvcGUiOlsiY3VzdG9kaWFuLnJlYWQiLCJjdXN0b2RpYW4ud3JpdGUiLCJhZHZpc2UucmVhZCIsImFkdmlzZS53cml0ZSIsImNoYW5uZWwucmVhZCIsImNoYW5uZWwud3JpdGUiLCJtZXJjaGFudC5yZWFkIiwibWVyY2hhbnQud3JpdGUiLCJwYXltZW50LnJlYWQiLCJwYXltZW50LndyaXRlIiwiY2xlYXJpbmcucmVhZCIsImNsZWFyaW5nLndyaXRlIiwicmVjb25jaWxpYXRpb24ucmVhZCIsInJlY29uY2lsaWF0aW9uLndyaXRlIiwib3JkZXIucmVhZCIsIm9yZGVyLndyaXRlIl0sImV4cCI6MzY3NTY1Mjc1MSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9NRVJDSEFOVF9BRE1JTiJdLCJqdGkiOiJkYTZlZTU3ZC1kNTdkLTQyNTQtOWQ3MC1lZmFjY2Y5YmZjODYiLCJjbGllbnRfaWQiOiJzaW11bGF0b3ItY3JlZCJ9.TiB739KogijD3AIg0rNTJFtfXeEpheZIUp5jLI_NFYQ'
headers ={"Authorization":Authorization,"Content-Type":"application/json","Accept":"application/json"}

data ={
  # "merchantId": "8fa029c4-6b87-4a84-ab3a-a0b8a9dc9229", #租赁测试账户
  # "merchantId": "e990ebd3-b56f-4b44-abfc-e4f54d6cf657", #测试账户
  "merchantId": "1101401d-d707-45a4-aec6-5b3aadf04bed", #测试账户
  "no":var.timestamp,
  "paymentType": "LFTPAY",
  "transactionType": "CHARGE",
  "callbackUrl": "https://www.baidu.com",
  "transaction":{
    "serialNo": "123456",
    "amount": 100.00,
    "identityId": "1055018573489111040"
    }
  }

s = requests.post(url, data=json.dumps(data), headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)
# print(t['data'])

