#coding:utf-8

import requests
import time
import json
import re
import jiami
import hashlib
import xlrd
from datetime import date,datetime
from xlrd import open_workbook
from xlutils.copy import copy
import random
import re



# def request(url,data):
#     num = random.randint(100, 999)
#     timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime()) +str(num)
#     s = appid + '&' + json.dumps(data) + '&' + timestamp + '&' + key
#     print('加密报文：' + s)
#
#     sign = jiami.md5(s)
#
#     d = {'appId':appid, 'data':json.dumps(data),'sign':sign,'timestamp':timestamp}
#     print('入参data:'+d['data'])
#     data = json.dumps(d)
#     print('请求报文：'+data)
#     headers ={"Content-Type":"application/json"}
#
#     s = requests.post(url,data=data,headers=headers)
#     print('接口状态：'+str(s.status_code))
#     print('返回报文：'+s.text)
#     return s.text



############加密###################
def md5(s):
    md5 = hashlib.md5()
    sign_bytes_utf8 = s.encode(encoding="utf-8")
    md5.update(sign_bytes_utf8)
    sign = md5.hexdigest()
    print('加密结果：'+sign)
    return sign

# 写数据
def write(r,c,datas):
    rb = open_workbook(r'D:\juhe\xieyinew\data\1.xls')

    #通过sheet_by_index()获取的sheet没有write()方法
    rs = rb.sheet_by_index(0)
    wb = copy(rb)

    #通过get_sheet()获取的sheet有write()方法
    ws = wb.get_sheet(0)
    ws.write(r, c, datas)

    wb.save(r'D:\juhe\xieyinew\data\1.xls')


# 读数据
wb = xlrd.open_workbook(r'D:\juhe\xieyinew\data\1.xls')
table = wb.sheets()[0]
nrows = table.nrows
ncols = table.ncols
appid = []
channelType = []
transDesc = []
businessId = []
key = []
yq = []
for rownum in range(table.nrows-1):
    ap = table.row(rownum + 1)[0].value
    ch = table.row(rownum + 1)[5].value
    tr = table.row(rownum + 1)[6].value
    bu = table.row(rownum + 1)[7].value
    k = table.row(rownum + 1)[9].value
    y = table.row(rownum + 1)[11].value
    appid.append(ap)
    channelType.append(ch)
    transDesc.append(tr)
    businessId.append(bu)
    key.append(k)
    yq.append(y)

print('appid:'+ str(appid))
print('channelType:'+str(channelType))
print('transDesc:'+str(transDesc))
print('businessId:'+str(businessId))
print('key:'+str(key))
print('yq:'+str(yq))


datass =[]
ss = []
print('--------------------------')
num = random.randint(100, 999)
timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(num)
for i in range(nrows-1):
    print('appid:'+appid[i],'channelType:'+channelType[i],'transDesc:'+transDesc[i],'businessId:'+businessId[i],'key:'+key[i])


    data = {"transDesc":transDesc[i],"businessId":businessId[i],"channelType":channelType[i]}
    # print(data)
    # print(timestamp)
    s = appid[i] + '&' + json.dumps(data) + '&' + timestamp + '&' + key[i]
    print('data:'+json.dumps(data))
    print('timestamp:'+timestamp)
    print('加密报文：' + s)
    print('--------------------------')
    datass.append(data)
    ss.append(s)

#加密
sign = []
print('++++++++++++++++')
for i in range(nrows-1):
    si = md5(ss[i])
    write(i+1,1,str(datass[i]))
    write(i+1,3,str(timestamp))
    write(i+1,2,str(si))
    sign.append(si)


#创建协议请求地址
url = 'http://172.29.66.21:80/api/protocol/create'

headers ={"Content-Type":"application/json"}
for i in range(nrows-1):
    d = {'appId':appid[i], 'data':json.dumps(datass[i]),'sign':sign[i],'timestamp':timestamp}
    dat = json.dumps(d)
    s1s = requests.post(url,data=dat,headers=headers)
    print('接口状态：'+str(s1s.status_code))
    print('返回报文：'+s1s.text)


    t = s1s.text

    # ssss = json.loads(t)
    #
    # code = list(ssss.items())[0][0]
    # value = list(ssss.items())[0][1]
    # sj = code +':' +value
    # print(sj)
    #
    # write(i+1,13,str(sj))

    # if str(yq[i]) == str(sj):
    #     write(i+1, 15, 'pass')
    # else:
    #     write(i+1, 15, 'fail')

    print(re.findall(yq[i], t))
    if len(re.findall(yq[i], t)):
        write(i+1, 15, 'pass')
    else:
        write(i+1, 15, 'fail')
