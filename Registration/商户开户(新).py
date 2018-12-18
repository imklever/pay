'''
涉及表：
merchant   payment
payment_order_notification 回调ke
payment_order_notification 这张表按notification_type=MERCHANT_ORDER & created_time
定时器
merchantUpsertTrigger 创建商户
merchantQueryJob 查询商户状态
'''

import requests
import time
import json
import random
import var


print(var.timestamp)
# no = time.strftime("%Y%m%d%H%M%S", time.localtime())
# print(no)

Authorization ='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiYXJjaGltb25kZSJdLCJ1c2VyX25hbWUiOiJtZXJjaGFudC5hZG1pbkBia2prLXRlc3QuY29tIiwic2NvcGUiOlsiY3VzdG9kaWFuLnJlYWQiLCJjdXN0b2RpYW4ud3JpdGUiLCJhZHZpc2UucmVhZCIsImFkdmlzZS53cml0ZSIsImNoYW5uZWwucmVhZCIsImNoYW5uZWwud3JpdGUiLCJtZXJjaGFudC5yZWFkIiwibWVyY2hhbnQud3JpdGUiLCJwYXltZW50LnJlYWQiLCJwYXltZW50LndyaXRlIiwiY2xlYXJpbmcucmVhZCIsImNsZWFyaW5nLndyaXRlIiwicmVjb25jaWxpYXRpb24ucmVhZCIsInJlY29uY2lsaWF0aW9uLndyaXRlIiwib3JkZXIucmVhZCIsIm9yZGVyLndyaXRlIl0sImV4cCI6MzY4MjM1MDg5MSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9NRVJDSEFOVF9BRE1JTiJdLCJqdGkiOiJmYmQwNmQ1NS0yN2ViLTQ5MGQtODkxYS03NThhYjBhYzRmZmQiLCJjbGllbnRfaWQiOiJzaW11bGF0b3ItdGVzdCJ9.KqLR2IWzIwVdA2ZbxQFQlfbv2yDZI6o_UawgTUBE-KA'
url = 'http://archimonde.dev.bkjk.cn/archimonde/api/merchants'
headers ={"Authorization":Authorization,"Content-Type":"application/json","Accept":'application/json'}
data = {
  "name": "测试账号18100905",
  "email": "klqlv997373@163.com",
  "remarks": "13",
  "type":"ENTERPRISE",
  "no":var.timestamp,
  "accountEmails":[{
    "email":"test12018100905@test.com",
    "type":"1"
  },
    {
      "email":"test22018100905@test.com",
      "type":"2"
  }
  ]
}


s = requests.post(url, data=json.dumps(data), headers=headers)
print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)


