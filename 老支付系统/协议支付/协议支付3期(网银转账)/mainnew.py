#coding:utf-8
import json
import random

import request
import time

print('####################创建协议开始##################')
##创建协议入参
data1 = {"transDesc":"test1","businessId":"2","channelType":"LFT"}
#创建协议请求地址
url1 = 'http://172.29.66.21:80/api/protocol/create'

t1 = request.request(url1, data1)

sss1 = json.loads(t1)
ss11 = sss1['data']
ss1 = json.loads(ss11)
transNo = ss1['transNo']
print('transNo:'+transNo,'amount:'+ss1['amount'],'onpassageAmount:'+ss1['onpassageAmount'],'outAmount:'+ss1['outAmount'])

print('####################创建协议结束##################')


print('####################查询协议开始##################')
##查询协议入参
data2 = {"transNo":transNo}
#查询协议请求地址
url2 = 'http://172.29.66.21:80/api/protocol/find'

t2 = request.request(url2, data2)

sss2 = json.loads(t2)
ss21 = sss2['data']
ss2 = json.loads(ss21)
print('transNo:'+transNo,'amount:'+ss2['amount'],'onpassageAmount:'+ss2['onpassageAmount'],'outAmount:'+ss2['outAmount'])

print('####################查询协议结束##################')


print('####################入金生成POS六位码开始##################')
##入金生成POS六位码入参
no = random.randint(1000000000,9999999999)
outReqNo = '10005'+str(no)
amount = '1000.00'
outArrivedNotifyUrl = 'www.baidu.com'
outSuccessNotifyUrl = 'www.baidu.com'
transNo = transNo
prodCatalog = '01'
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
print('####################等待入金状态更新######################')
time.sleep(60)
# print('####################入金关闭POS六位码开始##################')
# ##入金关闭POS六位码入参
# data4 = {"outReqNo":outReqNo}
# #入金关闭POS六位码请求地址
# url4 = 'http://172.29.66.21:80/api/protocol/posclose'
#
# t4 = request.request(url4,data4)
#
# # sss4 = json.loads(t4)
# # ss41 = sss4['data']
# # ss4 = json.loads(ss41)
# # print('transNo:'+transNo,'amount:'+ss4['amount'],'onpassageAmount:'+ss4['onpassageAmount'],'outAmount:'+ss4['outAmount'])
#
# print('####################入金关闭POS六位码结束##################')

flag = 1
while flag:
    print('####################入金查询开始##################')
    ##入金查询入参
    data5 = {"outReqNo":outReqNo}
    #入金查询请求地址
    url5 = 'http://172.29.66.21:80/api/protocol/inquery'

    t5 = request.request(url5, data5)

    sss5 = json.loads(t5)
    ss51 = sss5['data']
    ss5 = json.loads(ss51)
    print('transNo:'+transNo,'amount:'+ss5['amount'],'outReqNo:'+ss5['outReqNo'],'posCode:'+ss5['posCode'],'payStatus:'+ss5['payStatus'],'arrivedStatus:'+ss5['arrivedStatus'])

    print('####################入金查询结束##################')

    time.sleep(10)

    if ss5['payStatus'] != 'UNPAID':
        flag = 0

print('####################出金或退款开始##################')
##出金或退款入参
transNo = transNo
outReqNo = outReqNo
amount = '100.00'
channelType = 'LFT'
outNotifyUrl = 'www.baidu.com'
bankAccName = '李冉'
bankAccNum = '4349849854'
bankName = '中国银行'
bankCnaps = '100010'
outType = 'OUT'
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


print('####################出金或退款查询开始##################')
##出金或退款查询入参
data7 = {"outReqNo":outReqNo}
#出金或退款查询请求地址
url7 = 'http://172.29.66.21:80/api/protocol/outquery'

t7 = request.request(url7, data7)

sss7 = json.loads(t7)
ss71 = sss7['data']
ss7 = json.loads(ss71)
print('transNo:'+transNo,'amount:'+ss7['amount'],'outReqNo:'+ss7['outReqNo'],'outType:'+ss7['outType'],'payStatus:'+ss7['payStatus'])

print('####################出金或退款查询结束##################')


print('####################联行号查询开始##################')
##联行号查询入参
data8 = {"bankNameKeyWord":'海淀'}
#联行号查询请求地址
url8 = 'http://172.29.66.21:80/api/protocol/querybankcnaps'

t8 = request.request(url8, data8)

# sss8 = json.loads(t8)
# ss81 = sss8['data']
# ss8 = json.loads(ss81)
# print('transNo:'+transNo,'amount:'+ss8['amount'],'outReqNo:'+ss8['outReqNo'],'outType:'+ss8['outType'],'payStatus:'+ss8['payStatus'])

print('####################联行号查询结束##################')