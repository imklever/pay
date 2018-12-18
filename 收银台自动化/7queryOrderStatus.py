#coding:utf-8

import requests
import json
import para
import data

url = 'http://dev.cashier.zufangzi.com/cashierbe/bkjk/quickpay/queryOrderStatus'

headers ={"Authorization":para.Authorization,"Content-Type":"application/x-www-form-urlencoded"}

data1 = 'no='
data2 = '&token='
data3 = '&merchantId='
data = data1 + para.no + data2 + para.token + data3 + data.merchantId
# print(data)

s = requests.post(url, data=data, headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)

