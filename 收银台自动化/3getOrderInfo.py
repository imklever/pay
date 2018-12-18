#coding:utf-8

import requests
import json
import para

url1 = 'http://dev.cashier.zufangzi.com/cashierbe/bkjk/quickpay/getOrderInfo/v1?token='
token = para.token
url = url1+token

headers ={"Authorization":para.Authorization,"Content-Type":"application/json","sys-source":"CASHIER"}
s = requests.get(url, headers=headers)
# print(s.text)
print(s.url)
print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)
