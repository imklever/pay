#coding:utf-8

import hashlib
import json
import random

import requests
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy

import jiami
import time


def request(url,data):
    num = random.randint(100,999)
    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(num)
    s = appid + '&' + json.dumps(data) + '&' + timestamp + '&' + key
    print('加密报文：' + s)

    sign = jiami.md5(s)

    d = {'appId':appid, 'data':json.dumps(data),'sign':sign,'timestamp':timestamp}
    print('入参data:'+d['data'])
    data = json.dumps(d)
    print('请求报文：'+data)
    headers ={"Content-Type":"application/json"}

    s = requests.post(url,data=data,headers=headers)
    print('接口状态：'+str(s.status_code))
    print('返回报文：'+s.text)
    return s.text



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
appid = table.row(1)[0].value
channelType = table.row(1)[5].value
transDesc = table.row(1)[6].value
businessId = table.row(1)[7].value
key = table.row(1)[9].value
yq = table.row(1)[11].value
print('appid:'+appid,'channelType:'+channelType,'transDesc:'+transDesc,'businessId:'+businessId,'key:'+key)


data = {"transDesc":transDesc,"businessId":businessId,"channelType":channelType}
timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
s = appid + '&' + json.dumps(data) + '&' + timestamp + '&' + key
print('data:'+json.dumps(data))
print('timestamp:'+timestamp)
print('加密报文：' + s)

#加密
sign = md5(s)
write(1,1,str(data))
write(1,3,str(timestamp))
write(1,2,str(sign))


#创建协议请求地址
url = 'http://172.29.66.21:80/api/protocol/create'

headers ={"Content-Type":"application/json"}
d = {'appId':appid, 'data':json.dumps(data),'sign':sign,'timestamp':timestamp}
dat = json.dumps(d)
s1s = requests.post(url,data=dat,headers=headers)
print('接口状态：'+str(s1s.status_code))
print('返回报文：'+s1s.text)


t = s1s.text

ssss = json.loads(t)

code = list(ssss.items())[0][0]
value = list(ssss.items())[0][1]
sj = code +':' +value
print(sj)

write(1,13,str(sj))

if str(yq) == str(sj):
    write(1, 15, 'pass')
else:
    write(1, 15, 'fail')