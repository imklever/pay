#coding:utf-8
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import xlsxwriter

def write(r, c, datas):
    rb = xlsxwriter.Workbook(r'D:\juhe\收银台\云信通道路由\data\data2.xlsx')

    # 通过sheet_by_index()获取的sheet没有write()方法
    # rs = rb.sheet_by_index(0)
    wb = copy(rb)

    # 通过get_sheet()获取的sheet有write()方法
    ws = wb.get_sheet(0)
    ws.write(r, c, datas)

    wb.save(r'D:\juhe\收银台\云信通道路由\data\data1.xlsx')

write(1, 8, '49999.0可用通道：ALLINPAY')