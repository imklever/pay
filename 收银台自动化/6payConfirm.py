#coding:utf-8

import requests
import json
import para
import data

url = 'http://dev.cashier.zufangzi.com/cashierbe/bkjk/quickpay/payConfirm'

headers ={"Authorization":para.Authorization,"Content-Type":"application/x-www-form-urlencoded"}

data1 = 'merchantId='
data2 = '&no='
data3 = '&verificationCode=888888&identityId=1055007923228508160&cvvNumber=&validTime=&token='
data = data1 + data.merchantId + data2 + para.no + data3 + para.token
# print(data)

s = requests.post(url, data=data, headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)


