#coding:utf-8
import json
import random

import request

transNo = 'TR180712135909601631112'
# outReqNo = ''

print('####################出金或退款开始##################')
##出金或退款入参
no = random.randint(1000000000,9999999999)
outReqNo = '10005'+str(no)
transNo = transNo
amount = '100.00'
channelType = 'LFT'
outNotifyUrl = 'www.baidu.com'
bankAccName = '李冉'
bankAccNum = '4349849854'
bankName = '中国银行'
bankCnaps = '100010'
outType = 'REFUND'
remark = '付款描述'
data6 = {"transNo":transNo,"outReqNo":outReqNo,"amount":amount,"channelType":channelType,"outNotifyUrl":outNotifyUrl,"bankAccName":bankAccName,"bankAccNum":bankAccNum,"bankName":bankName,"bankCnaps":bankCnaps,"outType":outType,"remark":remark}

#出金或退款请求地址
url6 = 'http://172.29.66.21:80/api/protocol/outpay'

t6 = request.request(url6, data6)

sss6 = json.loads(t6)
ss61 = sss6['data']
ss6 = json.loads(ss61)
outReqNo = ss6['outReqNo']
print('transNo:'+transNo,'amount:'+ss6['amount'],'outReqNo:'+ss6['outReqNo'],'outType:'+ss6['outType'],'payStatus:'+ss6['payStatus'])

print('####################出金或退款结束##################')

print(len(sss6.keys()))
print(sss6.keys())
print(len(ss6.keys()))
print(ss6.keys())
