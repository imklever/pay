'''
入金接口
https://payment.test.bkjk.com/api/protocol/prepay
'''
#coding:utf-8
import json
import random
import time
import random

# timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
timestamp = time.strftime("%d%H%M%S", time.localtime())

import request

transNo = 'TR181214110848021462415'

print('####################入金生成POS六位码开始##################')
##入金生成POS六位码入参
no = random.randint(1000000000,9999999999)

transNo = transNo
outReqNo = '10005'+str(no)
amount = '10010.51'
outArrivedNotifyUrl = 'www.baidu.com'
outSuccessNotifyUrl = 'www.hao123.com'
prodCatalog = '02' #01只能借记卡;02借记卡;信用卡都可以 只对POS
contractNum = 'test'
qpUserName = 'test'+timestamp
# qpUserName = 'test'
cardNum = '62220202000205'+str(random.randint(10000,99999))
# cardNum = '6222020200020'
qpCertNumber = '279696197701257454'
returnUrl = 'www.baidu.com'

print(qpUserName,cardNum)

data3 = {"transNo":transNo,"outReqNo":outReqNo,"amount":amount,"outArrivedNotifyUrl":outArrivedNotifyUrl,"outSuccessNotifyUrl":outSuccessNotifyUrl,"prodCatalog":prodCatalog,"contractNum":contractNum,"qpUserName":qpUserName,"cardNum":cardNum,"qpCertNumber":qpCertNumber,"returnUrl":returnUrl}

#入金生成POS六位码请求地址
url3 = 'https://payment.test.bkjk.com/api/protocol/prepay'

t3 = request.request(url3, data3)

sss3 = json.loads(t3)
ss31 = sss3['data']
ss3 = json.loads(ss31)
outReqNo = ss3['outReqNo']
print('------')
if 'posCode' in ss3.keys():
    print('POS入金：')
    print('transNo:'+transNo,'amount:'+ss3['amount'],'outReqNo:'+ss3['outReqNo'],'cashierType:'+ss3['cashierType'],'posCode:'+ss3['posCode'],'payStatus:'+ss3['payStatus'],'payOrderNo:'+ss3['payOrderNo'])
elif ss3['cashierType'] == 'ONLINEBANK':
    print('网银转账：')
    print('transNo:'+transNo,'amount:'+ss3['amount'],'outReqNo:'+ss3['outReqNo'],'cashierType:'+ss3['cashierType'],'qpUserName:'+ss3['qpUserName'],'cardNum:'+ss3['cardNum'],'payStatus:'+ss3['payStatus'],'payOrderNo:'+ss3['payOrderNo'])
else:
    print('快捷入金：')
    print('transNo:'+transNo,'amount:'+ss3['amount'],'outReqNo:'+ss3['outReqNo'],'cashierType:'+ss3['cashierType'],'payStatus:'+ss3['payStatus'],'payOrderNo:'+ss3['payOrderNo'],'cashierUrl:'+ss3['cashierUrl'])
    print(ss3['cashierUrl'])
print('------')

print('####################入金生成POS六位码结束##################')

print(len(sss3.keys()))
print(sss3.keys())
print(len(ss3.keys()))
print(ss3.keys())