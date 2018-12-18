#coding:utf-8

from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook(r'D:\juhe\xieyinew\data\1.xls')

#通过sheet_by_index()获取的sheet没有write()方法
rs = rb.sheet_by_index(0)
print(rs)
wb = copy(rb)

#通过get_sheet()获取的sheet有write()方法
ws = wb.get_sheet(0)
print(ws)
ws.write(1, 1, 'changed!')
print(ws)

wb.save(r'D:\juhe\xieyinew\data\1.xls')