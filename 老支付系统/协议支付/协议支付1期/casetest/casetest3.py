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

#请求地址
url = 'http://172.29.66.21:80/api/protocol/create'
headers ={"Content-Type":"application/json"}

r = table.row_values(0)
# print(r)
# print(r.index('appId'))
for rownum in range(table.nrows-1):
    print('开始第'+str(rownum+1)+'行')
    print('-----------------')

    # appid = table.row(rownum + 1)[0].value
    # channelType = table.row(rownum + 1)[5].value
    # transDesc = table.row(rownum + 1)[6].value
    # businessId = table.row(rownum + 1)[7].value
    # key = table.row(rownum + 1)[9].value
    # yq = table.row(rownum + 1)[11].value

    appid = table.row(rownum + 1)[r.index('appId')].value
    channelType = table.row(rownum + 1)[r.index('channelType')].value
    transDesc = table.row(rownum + 1)[r.index('transDesc')].value
    businessId = table.row(rownum + 1)[r.index('businessId')].value
    key = table.row(rownum + 1)[r.index('key')].value
    yq = table.row(rownum + 1)[r.index('预期结果')].value

    print('appid:'+ str(appid))
    print('channelType:'+str(channelType))
    print('transDesc:'+str(transDesc))
    print('businessId:'+str(businessId))
    print('key:'+str(key))
    print('yq:'+str(yq))


    num = random.randint(100, 999)
    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(num)

    print('appid:'+appid,'channelType:'+channelType,'transDesc:'+transDesc,'businessId:'+businessId,'key:'+key)


    data = {"transDesc":transDesc,"businessId":businessId,"channelType":channelType}

    s = appid + '&' + json.dumps(data) + '&' + timestamp + '&' + key
    print('data:'+json.dumps(data))
    print('timestamp:'+timestamp)
    print('加密报文：' + s)


    sign = md5(s)
    # write(rownum+1,1,str(data))
    # write(rownum+1,3,str(timestamp))
    # write(rownum+1,2,str(sign))

    write(rownum+1,r.index('data'),str(data))
    write(rownum+1,r.index('timestamp'),str(timestamp))
    write(rownum+1,r.index('sign'),str(sign))

    d = {'appId':appid, 'data':json.dumps(data),'sign':sign,'timestamp':timestamp}
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
    write(rownum+1,r.index('实际结果'),re.findall(yq, t))

    # if str(yq[i]) == str(sj):
    #     write(i+1, 15, 'pass')
    # else:
    #     write(i+1, 15, 'fail')

    # print(re.findall(yq, t))
    if len(re.findall(yq, t)):
        write(rownum+1, r.index('测试结果'), 'pass')
    else:
        write(rownum+1, r.index('测试结果'), 'fail')

    print('-----------------')
    print('结束第'+str(rownum+1)+'行')

