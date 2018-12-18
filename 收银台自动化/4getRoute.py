#coding:utf-8

import requests
import json
import para

url = 'http://dev.cashier.zufangzi.com/cashierbe/bkjk/quickpay/getRoute'

headers ={"Authorization":para.Authorization,"Content-Type":"application/x-www-form-urlencoded"}

data1 ='bankAccountNo=9003090211230192&bankAcronym=CEB&bankCardType=DEBIT_CARD&token='
token = para.token
data = data1+token

s = requests.post(url, data=data, headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)
# print(t['data'])

