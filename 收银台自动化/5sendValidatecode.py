#coding:utf-8

import requests
import json
import para
import data


url = 'http://dev.cashier.zufangzi.com/cashierbe/bkjk/quickpay/sendValidatecode'

headers ={"Authorization":para.Authorization,"Content-Type":"application/x-www-form-urlencoded"}

data1 = 'merchantId='
data2 = '&no='
data3 = '&token='
data4 = '&bankAcronym=CEB&bankAccountNo=9003090211230192&bankAccountName=%E6%9D%A8%E6%B5%B7%E6%B7%98&idNo=51052219860514523X&reservedPhone=15811293212&bankCardType=DEBIT_CARD&identityId=1055007923228508160&cvvNumber=&validTime=&amount='
data5 = '&description=&remark='
merchantId = data.merchantId
no = para.no
token = para.token
data = data1+merchantId+data2+no+data3+token+data4+data.amount+data5
# print(data)

s = requests.post(url, data=data, headers=headers)
# print(s.status_code)
t = s.json()
# print(t)
js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'),ensure_ascii=False)
print(js)
# print(t['data'])

