#coding:utf-8

import xlrd

#将excel文件数据转换为dict
def get_data(filename, sheetnum):
    dir_case = 'D:\\pay\\协议支付1期\\data\\' + filename + '.xls'
    data = xlrd.open_workbook(dir_case)
    table = data.sheets()[sheetnum]
    nor = table.nrows
    nol = table.ncols
    dict = {}
    list = []
    for i in range(1, nor):
        for j in range(nol):
            title = table.cell_value(0, j)
            value = table.cell_value(i, j)
            dict[title] = value
        yield dict



if __name__ == '__main__':
    for i in get_data('1', 0):
        print(i)


