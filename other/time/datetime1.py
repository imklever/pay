#coding:utf-8

'''
datetime比time高级了不少，可以理解为datetime基于time进行了封装，提供了更为适用的函数，datetime模块的接口更直观，更容易调用

模块中的类：
datetime 同时有时间和日期
timedelta 主要用于计算时间的跨度
tzinfo 时区相关
time 只关注时间
date 只关注日期
'''

import datetime

#获取当前时间
d1 = datetime.datetime.now()
print(d1)
print(type(d1))

#获取指定时间
d2 = datetime.datetime(2000,10,1,10,28,26,111111)
print(d2)

#将时间转为字符串
d3 = d1.strftime("%Y-%m-%d %X")
print(d3)
print(type(d3))

#将格式化字符串转为datetime对象
d4 = datetime.datetime.strptime(d3,"%Y-%m-%d %X")
print(d4)
print(type(d4))

d5 = datetime.datetime(2000,10,1,10,28,26,111111)
d6 = datetime.datetime.now()
d7 = d6 - d5
print(d7)
print(type(d7))
#间隔的天数
print(d7.days)
#间隔天数除外的秒数
print(d7.seconds)