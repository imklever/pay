#coding:utf-8

import xlrd
from datetime import date,datetime

# 文件位置
wb = xlrd.open_workbook(r'D:\juhe\xieyinew\data\1.xls')
# 获取目标EXCEL文件sheet名
print(wb.sheet_names())
#选择某一个工作表（通过索引或表名称）
# 获取第一个工作表
table = wb.sheets()[0]
# # 通过索引获取第一个工作表
# table = wb.sheet_by_index(0)
# # 通过表名称选择工作表
# table = wb.sheet_by_name(u'Sheet1')
print(table)
# 获取表格的行数和列数
nrows = table.nrows
ncols = table.ncols
print(nrows,ncols)
# 获取整行和整列的值
r = table.row_values(0)
print(r)
c = table.col_values(1)
print(c)
# 通过循环读取表格的所有行
for rownum in range(table.nrows):
    print(table.row_values(rownum))
# 通过循环读取表格的所有列
for colnum in range(table.ncols):
    print(table.col_values(colnum))
# 获取单元格的值
cell_A11 = table.row(0)[0].value
# 或者像下面这样
cell_A12 = table.cell(0, 0).value
# 或者像下面这样通过列索引
cell_A13 = table.col(0)[0].value
print(cell_A11,cell_A12,cell_A13)