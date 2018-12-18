#coding:utf-8
import json

import request

outReqNo = '100052138654725'

print('####################入金查询开始##################')
##入金查询入参
data5 = {"outReqNo": outReqNo}
# 入金查询请求地址
url5 = 'http://172.29.66.21:80/api/protocol/inquery'

t5 = request.request(url5, data5)

sss5 = json.loads(t5)
ss51 = sss5['data']
ss5 = json.loads(ss51)
print( 'amount:' + ss5['amount'], 'outReqNo:' + ss5['outReqNo'], 'posCode:' + ss5['posCode'],
      'payStatus:' + ss5['payStatus'], 'arrivedStatus:' + ss5['arrivedStatus'])

print('####################入金查询结束##################')

print(len(sss5.keys()))
print(sss5.keys())
print(len(ss5.keys()))
print(ss5.keys())