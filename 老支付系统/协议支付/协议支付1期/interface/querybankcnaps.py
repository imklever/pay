#coding:utf-8
import json
import re

import request

print('####################联行号查询开始##################')
##联行号查询入参
data8 = {"bankNameKeyWord":'海淀'}
#联行号查询请求地址
url8 = 'http://172.29.66.21:80/api/protocol/querybankcnaps'

t8 = request.request(url8, data8)

sss8 = json.loads(t8)
ss81 = sss8['data']
ss8 = json.loads(ss81)
# print('transNo:'+transNo,'amount:'+ss8['amount'],'outReqNo:'+ss8['outReqNo'],'outType:'+ss8['outType'],'payStatus:'+ss8['payStatus'])

print('####################联行号查询结束##################')

print(len(sss8.keys()))
print(sss8.keys())
print(len(ss8))
# aa = re.findall("'bankCardType': '(.+?)'" ,str(yy))
aa = re.findall('"bankName":"(.+?)"',str(ss81))
print(aa)
for i in range(len(aa)):
    print(aa[i])


