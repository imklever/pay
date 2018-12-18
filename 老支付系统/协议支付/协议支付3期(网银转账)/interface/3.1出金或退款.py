'''
出金或退款接口
https://payment.test.bkjk.com/api/protocol/outpay
'''
#coding:utf-8
import json
import random

import request

transNo = 'TR181213200359337211333'
# outReqNo = ''

print('####################出金或退款开始##################')
##出金或退款入参
no = random.randint(1000000000,9999999999)
outReqNo = '10005'+str(no)
transNo = transNo
amount = '15.00'
channelType = 'LFT'
outNotifyUrl = 'www.baidu.com'
bankAccName = 'test'
bankAccNum = '4349849854'
bankName = '中国银行'
bankCnaps = '100010'
outType = 'OUT'
remark = '付款描述'
data6 = {"transNo":transNo,"outReqNo":outReqNo,"amount":amount,"channelType":channelType,"outNotifyUrl":outNotifyUrl,"bankAccName":bankAccName,"bankAccNum":bankAccNum,"bankName":bankName,"bankCnaps":bankCnaps,"outType":outType,"remark":remark}

#出金或退款请求地址
url6 = 'https://payment.test.bkjk.com/api/protocol/outpay'

t6 = request.request(url6, data6)

sss6 = json.loads(t6)
ss61 = sss6['data']
ss6 = json.loads(ss61)
outReqNo = ss6['outReqNo']
print('------')
if 'channelReturnCode' in ss6.keys():
    print('channelReturnCode:'+ss6['channelReturnCode'],'channelReturnMsg:'+ss6['channelReturnMsg'])
print('transNo:'+transNo,'amount:'+ss6['amount'],'outReqNo:'+ss6['outReqNo'],'outType:'+ss6['outType'],'payStatus:'+ss6['payStatus'],'payOrderNo:'+ss6['payOrderNo'])
print('bankAccName:'+ss6['bankAccName'],'bankAccNum:'+ss6['bankAccNum'],'bankName:'+ss6['bankName'],'bankCnaps:'+ss6['bankCnaps'])
print('------')

print('####################出金或退款结束##################')

print(len(sss6.keys()))
print(sss6.keys())
print(len(ss6.keys()))
print(ss6.keys())
