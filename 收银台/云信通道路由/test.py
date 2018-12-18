#coding:utf-8
'''
云信绑还款卡路由
ALLINPAY 通联 CFCAPAY 中金
'''

import random
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import xlwt

import requests
import time
import json
import random
import var
import re

Authorization ='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiYXJjaGltb25kZSJdLCJ1c2VyX25hbWUiOiJtZXJjaGFudC5hZG1pbkBia2prLXRlc3QuY29tIiwic2NvcGUiOlsiY3VzdG9kaWFuLnJlYWQiLCJjdXN0b2RpYW4ud3JpdGUiLCJhZHZpc2UucmVhZCIsImFkdmlzZS53cml0ZSIsImNoYW5uZWwucmVhZCIsImNoYW5uZWwud3JpdGUiLCJtZXJjaGFudC5yZWFkIiwibWVyY2hhbnQud3JpdGUiLCJwYXltZW50LnJlYWQiLCJwYXltZW50LndyaXRlIiwiY2xlYXJpbmcucmVhZCIsImNsZWFyaW5nLndyaXRlIiwicmVjb25jaWxpYXRpb24ucmVhZCIsInJlY29uY2lsaWF0aW9uLndyaXRlIiwib3JkZXIucmVhZCIsIm9yZGVyLndyaXRlIl0sImV4cCI6MzY4MjM1MDg5MSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9NRVJDSEFOVF9BRE1JTiJdLCJqdGkiOiJmYmQwNmQ1NS0yN2ViLTQ5MGQtODkxYS03NThhYjBhYzRmZmQiLCJjbGllbnRfaWQiOiJzaW11bGF0b3ItdGVzdCJ9.KqLR2IWzIwVdA2ZbxQFQlfbv2yDZI6o_UawgTUBE-KA'

url1 = 'http://archimonde.dev.bkjk.cn/archimonde/api/advises/selected-payment?paymentCategory=FASTPAY&transactionType=CHARGE&bankAccountType=PRIVATE&requestedAmount='
url2 = '&bankAcronym='
url3 = '&bankAccountNo=6226095711989751&merchantId=e990ebd3-b56f-4b44-abfc-e4f54d6cf657&enableTrace=true&bankCardType=DEBIT_CARD'
headers ={"Authorization":Authorization,"Content-Type":"application/json"}

def request(am,ba):
    url = url1 + am + url2 + ba + url3
    s = requests.get(url, headers=headers)
    # print(s.status_code)
    t = s.json()
    # # print(t)
    # js = json.dumps(t, sort_keys=False, indent=4, separators=(',', ':'), ensure_ascii=False)
    try:
        if t['code'] == 'BR1100':
            # print('没有可用通道')
            return '没有可用通道'
    except:
        print()

    try:
        if t['code'] == 'BR2000':
            # print('可用通道：' + t['content']['sections'][0]['paymentType'])
            return '可用通道：' + t['content']['sections'][0]['paymentType']
    except:
        print()

# # 写数据
# def write(r, c, datas):
#     rb = open_workbook(r'D:\pay\收银台\云信通道路由\data\data1.xlsx')
#
#     # 通过sheet_by_index()获取的sheet没有write()方法
#     # rs = rb.sheet_by_index(0)
#     wb = copy(rb)
#
#     # 通过get_sheet()获取的sheet有write()方法
#     ws = wb.get_sheet(0)
#     ws.write(r, c, datas)
#
#     wb.save(r'D:\pay\收银台\云信通道路由\data\data1.xlsx')

# 写数据
def write(r, c, datas):
    # 打开想要更改的excel文件
    old_excel = xlrd.open_workbook('data\data2.xls')
    # 将操作文件对象拷贝，变成可写的workbook对象
    new_excel = copy(old_excel)
    # 获得第一个sheet的对象
    ws = new_excel.get_sheet(2)
    # # 写入数据
    ws.write(r, c, datas)
    # 另存为excel文件，并将文件命名
    new_excel.save('data\data2.xls')


# 读数据
wb = xlrd.open_workbook(r'D:\juhe\收银台\云信通道路由\data\data2.xls')
table = wb.sheets()[2]
n = table.nrows
print(n)

for i in range(1,n):
    bank = table.row(i)[6].value
    # print(bank)
    amount1 = table.row(i)[1].value
    # print(amount1)
    amount2 = table.row(i)[4].value
    # print(amount2)

    print('开始执行第'+str(i)+'行。。。')
    case = []
    if (amount1 != '' and amount2 == ''):
        amount = amount1 * 10000
        n1 = amount-1
        n2 = amount
        n3 = amount+1
        case.append(n1)
        case.append(n2)
        case.append(n3)
    elif (amount1 == '' and amount2 != ''):
        amount = amount2 * 10000
        n1 = amount-1
        n2 = amount
        n3 = amount+1
        case.append(n1)
        case.append(n2)
        case.append(n3)
    elif (amount1 == '' and amount2 == ''):
        n1 = 1
        case.append(n1)
    elif float(amount1) == float(amount2):
        amount = amount1 * 10000
        n1 = amount-1
        n2 = amount
        n3 = amount+1
        case.append(n1)
        case.append(n2)
        case.append(n3)
    elif float(amount1) != float(amount2):
        min = amount1 * 10000
        max = amount2 * 10000
        if amount2 < amount1:
            min = amount2 * 10000
            max = amount1 * 10000
        n1 = min - 1
        n2 = min
        n3 = min + 1
        n4 = max
        n5 = max + 1
        case.append(n1)
        case.append(n2)
        case.append(n3)
        case.append(n4)
        case.append(n5)

    ii = 8
    for l in case:
        print(l,request(str(l), bank))
        try:
            write(i, ii, (str(l)+request(str(l), bank)))
        except:
            pass
        ii += 1

    # for l in case:
    #     # print(l)
    #     print(str(l)+request(str(l), bank))

    time.sleep(3)

