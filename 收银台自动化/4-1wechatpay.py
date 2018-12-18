#coding:utf-8

import requests
import json
import para

url = 'http://dev.cashier.zufangzi.com/cashierbe/bkjk/wechatpay/createOrder/v1'

headers ={"Authorization":para.Authorization,"Content-Type":"application/x-www-form-urlencoded"}

data1 = 'token='
data2 = '&productCode=WX_PUBLIC_ACCOUNT'
token = para.token
data = data1+token+data2

s = requests.post(url, data=data, headers=headers)
print(s.url)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)
# print(t['data'])

