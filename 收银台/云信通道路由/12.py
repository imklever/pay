#coding:utf-8
# import xlrd
# from xlrd import open_workbook
# from xlutils.copy import copy
# import xlsxwriter
#
# def write(a, datas):
#     rb = xlsxwriter.Workbook(r'D:\pay\收银台\云信通道路由\data\data2.xls')
#
#     w =rb.add_worksheet('sheet1')
#     w.write(a, datas)
#     rb.close()
#
# write('I2', '49999.0可用通道：ALLINPAY')


# from xlutils.copy import copy
# import xlrd
# #xlutils:修改excel
# book1 = xlrd.open_workbook(r'D:\pay\收银台\云信通道路由\data\data2.xlsx')
# book2 = copy(book1)#拷贝一份原来的excel
# # print(dir(book2))
# sheet = book2.get_sheet(0)#获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的
# # sheet.write(1,3,0)
# sheet.write(1, 8, '49999.0可用通道：ALLINPAY')
# book2.save('D:\pay\收银台\云信通道路由\data\data2.xlsx')

# import xlrd                           #导入模块
# from xlutils.copy import copy        #导入copy模块
# rb = xlrd.open_workbook('data\data2.xlsx')    #打开weng.xls文件
# wb = copy(rb)                          #利用xlutils.copy下的copy函数复制
# ws = wb.get_sheet(0)                   #获取表单0
# # ws.write(0, 0, 'changed!')             #改变（0,0）的值
# ws.write(1, 8,label = '49999.0可用通道：ALLINPAY')           #增加（8,0）的值
# wb.save('data\data2.xlsx')

import xlrd
import xlwt
from xlutils.copy import copy

# 打开想要更改的excel文件
old_excel = xlrd.open_workbook('data\data1.xlsx')
# 将操作文件对象拷贝，变成可写的workbook对象
new_excel = copy(old_excel)
# 获得第一个sheet的对象
ws = new_excel.get_sheet(0)
# # 写入数据
# ws.write(1, 8, '49999.0可用通道：ALLINPAY')
# 另存为excel文件，并将文件命名
new_excel.save('data\data2.xls')
