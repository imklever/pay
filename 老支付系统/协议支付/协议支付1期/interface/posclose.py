#coding:utf-8
import json

import request

outReqNo = '100059242498789'

print('####################入金关闭POS六位码开始##################')
##入金关闭POS六位码入参
data4 = {"outReqNo":outReqNo}
#入金关闭POS六位码请求地址
url4 = 'http://172.29.66.21:80/api/protocol/posclose'

t4 = request.request(url4, data4)

sss4 = json.loads(t4)
ss41 = sss4['data']
ss4 = json.loads(ss41)

print('####################入金关闭POS六位码结束##################')

print(len(sss4.keys()))
print(sss4.keys())
print(len(ss4.keys()))
print(ss4.keys())