'''
出金或退款查询接口
https://payment.test.bkjk.com/api/protocol/outquery
'''
#coding:utf-8
import json

import request

outReqNo = '10005509061635160145920'

print('####################出金或退款查询开始##################')
##出金或退款查询入参
data7 = {"outReqNo":outReqNo}
#出金或退款查询请求地址
url7 = 'https://payment.test.bkjk.com/api/protocol/outquery'

t7 = request.request(url7, data7)

sss7 = json.loads(t7)
ss71 = sss7['data']
ss7 = json.loads(ss71)
print('------')
if 'channelReturnCode' in ss7.keys():
    print('channelReturnCode:'+ss7['channelReturnCode'],'channelReturnMsg:'+ss7['channelReturnMsg'])
print('transNo:'+ss7['transNo'],'amount:'+ss7['amount'],'outReqNo:'+ss7['outReqNo'],'outType:'+ss7['outType'],'payStatus:'+ss7['payStatus'],'payOrderNo:'+ss7['payOrderNo'])
print('bankAccName:'+ss7['bankAccName'],'bankAccNum:'+ss7['bankAccNum'],'bankName:'+ss7['bankName'],'bankCnaps:'+ss7['bankCnaps'])
print('------')

print('####################出金或退款查询结束##################')

print(len(sss7.keys()))
print(sss7.keys())
print(len(ss7.keys()))
print(ss7.keys())