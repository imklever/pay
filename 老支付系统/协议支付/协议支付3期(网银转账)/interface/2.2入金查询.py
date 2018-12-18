'''
入金查询接口
https://payment.test.bkjk.com/api/protocol/inquery
'''
#coding:utf-8
import json

import request
# coding:utf-8
import json

import request

outReqNo = '100058714298877'

print('####################入金查询开始##################')
##入金查询入参
data5 = {"outReqNo": outReqNo}
# 入金查询请求地址
url5 = 'https://payment.test.bkjk.com/api/protocol/inquery'

t5 = request.request(url5, data5)

sss5 = json.loads(t5)
ss51 = sss5['data']
ss5 = json.loads(ss51)
print('------')
if 'posCode' in ss5.keys():
      print('POS入金：')
      print('transNo:'+ss5['transNo'], 'amount:' + ss5['amount'], 'outReqNo:' + ss5['outReqNo'], 'posCode:' + ss5['posCode'],
             'payStatus:' + ss5['payStatus'], 'arrivedStatus(资金到账状态01未到账02已到账):' + ss5['arrivedStatus'])
      print('cardNum:'+ss5['cardNum'],'issuingBank:'+ss5['issuingBank'],'issuingBankZH(发卡行(中文)):' + ss5['issuingBankzh'])
if ss5['cashierType'] == 'ONLINEBANK':
      print('网银转账：')
      print('transNo:'+ss5['transNo'], 'amount:' + ss5['amount'], 'outReqNo:' + ss5['outReqNo'],
             'payStatus:' + ss5['payStatus'], 'arrivedStatus(资金到账状态01未到账02已到账):' + ss5['arrivedStatus'])
      print('cardNum:'+ss5['cardNum'])

else:
      print('快捷入金：')
      print('transNo:'+ss5['transNo'],'amount:' + ss5['amount'], 'outReqNo:' + ss5['outReqNo'], 'payStatus:' + ss5['payStatus'],
            'arrivedStatus(资金到账状态01未到账02已到账):' + ss5['arrivedStatus'])
      print('cardNum:'+ss5['cardNum'],'issuingBankZH(发卡行(中文)):' + ss5['issuingBankzh'], 'qpUserName:' + ss5['qpUserName'], 'qpCertNumber:' + ss5['qpCertNumber'])
      print(ss5['cashierUrl'])
print('------')

print('####################入金查询结束##################')

print(len(sss5.keys()))
print(sss5.keys())
print(len(ss5.keys()))
print(ss5.keys())