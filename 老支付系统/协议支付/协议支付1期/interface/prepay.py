#coding:utf-8
import json
import random

import request

transNo = 'TR180712135909601631112'

print('####################入金生成POS六位码开始##################')
##入金生成POS六位码入参
no = random.randint(1000000000,9999999999)
outReqNo = '10005'+str(no)
# outReqNo = '100057105227791'
amount = '2000.00'
outArrivedNotifyUrl = 'www.baidu.com'
outSuccessNotifyUrl = 'www.baidu.com'
transNo = transNo
prodCatalog = '02'
data3 = {"outReqNo":outReqNo,"amount":amount,"outArrivedNotifyUrl":outArrivedNotifyUrl,"outSuccessNotifyUrl":outSuccessNotifyUrl,"transNo":transNo,"prodCatalog":prodCatalog}

#入金生成POS六位码请求地址
url3 = 'http://172.29.66.21:80/api/protocol/prepay'

t3 = request.request(url3, data3)

sss3 = json.loads(t3)
ss31 = sss3['data']
ss3 = json.loads(ss31)
outReqNo = ss3['outReqNo']
print('transNo:'+transNo,'amount:'+ss3['amount'],'outReqNo:'+ss3['outReqNo'],'posCode:'+ss3['posCode'],'payStatus:'+ss3['payStatus'])

print('####################入金生成POS六位码结束##################')

print(len(sss3.keys()))
print(sss3.keys())
print(len(ss3.keys()))
print(ss3.keys())