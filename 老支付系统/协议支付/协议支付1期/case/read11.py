#coding:utf-8

import xlrd
from datetime import date,datetime

# 文件位置
wb = xlrd.open_workbook(r'D:\juhe\xieyinew\data\1.xls')
# 获取第一个工作表
table = wb.sheets()[0]
# 获取表格的行数和列数
nrows = table.nrows
ncols = table.ncols
# print(nrows,ncols)
# 获取整行和整列的值
r = table.row_values(0)
print(r)
# for i in r:
#     print(i,r.index(i))


for i in r:
    for j in r:
        if i == j:
            n = r.index(i)
            print(i,n)

# # c = table.col_values(1)
# # print(c)
# # 通过循环读取表格的所有行
# appid = []
# for rownum in range(table.nrows-1):
#     t = table.row(rownum + 1)[0].value
#     appid.append(t)
# # # 通过循环读取表格的所有列
# # for colnum in range(table.ncols):
# #     print(table.col_values(colnum))
# #     appid = appid.append(table.row(rownum+1)[0].value)
# print(appid)
#
# for i in range(len(appid)):
#     print(appid[i])