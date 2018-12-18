#coding:utf-8

import requests
import time
import json
import random

# no = time.strftime("%Y%m%d%H%M%S", time.localtime())

Authorization ='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiYXJjaGltb25kZSJdLCJ1c2VyX25hbWUiOiJtZXJjaGFudC5hZG1pbkBia2prLWNyZWQuY29tIiwic2NvcGUiOlsiY3VzdG9kaWFuLnJlYWQiLCJjdXN0b2RpYW4ud3JpdGUiLCJhZHZpc2UucmVhZCIsImFkdmlzZS53cml0ZSIsImNoYW5uZWwucmVhZCIsImNoYW5uZWwud3JpdGUiLCJtZXJjaGFudC5yZWFkIiwibWVyY2hhbnQud3JpdGUiLCJwYXltZW50LnJlYWQiLCJwYXltZW50LndyaXRlIiwiY2xlYXJpbmcucmVhZCIsImNsZWFyaW5nLndyaXRlIiwicmVjb25jaWxpYXRpb24ucmVhZCIsInJlY29uY2lsaWF0aW9uLndyaXRlIiwib3JkZXIucmVhZCIsIm9yZGVyLndyaXRlIl0sImV4cCI6MzY3NTY1Mjc1MSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9NRVJDSEFOVF9BRE1JTiJdLCJqdGkiOiJkYTZlZTU3ZC1kNTdkLTQyNTQtOWQ3MC1lZmFjY2Y5YmZjODYiLCJjbGllbnRfaWQiOiJzaW11bGF0b3ItY3JlZCJ9.TiB739KogijD3AIg0rNTJFtfXeEpheZIUp5jLI_NFYQ'
url = 'http://archimonde.dev.bkjk.cn/archimonde/api/merchants'
headers ={"Authorization":Authorization,"Content-Type":"application/json","Accept":'application/json'}
data = {
  "no": "20180720111206",
  # "parentMerchantId":"ed97de45-f8e3-4441-9041-6816ca984f0a",
  "name": "贝壳小贷测试20180720111206",
  "type": "PERSONAL",
  "address": "上海市新天地贝壳小贷",
  "legalPersonName": "string",
  "legalPersonPhone": "11111111111",
  "legalPersonIdNo": "340222222222222222",
  "legalPersonIdType": "ID_CARD",
  "legalPersonIdBeginDate": "2018-01-01",
  "legalPersonIdEndDate": "9999-01-01",
  "legalPersonPictureUrls": "test",
  "remarks": "string",
  "callbackUrl": "string"
}

s = requests.post(url, data=json.dumps(data), headers=headers)
print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)


