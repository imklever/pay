#coding:utf-8
import json

import request

outReqNo = '100052501916221'

print('####################出金或退款查询开始##################')
##出金或退款查询入参
data7 = {"outReqNo":outReqNo}
#出金或退款查询请求地址
url7 = 'http://172.29.66.21:80/api/protocol/outquery'

t7 = request.request(url7, data7)

sss7 = json.loads(t7)
ss71 = sss7['data']
ss7 = json.loads(ss71)
print('transNo:'+ss7['transNo'],'amount:'+ss7['amount'],'outReqNo:'+ss7['outReqNo'],'outType:'+ss7['outType'],'payStatus:'+ss7['payStatus'])

print('####################出金或退款查询结束##################')

print(len(sss7.keys()))
print(sss7.keys())
print(len(ss7.keys()))
print(ss7.keys())