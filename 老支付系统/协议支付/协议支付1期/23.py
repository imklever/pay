#coding:utf-8

# def func1():
#     print("dddd")
#
# def outer(func):
#     def inner():
#         print('+++++++++++++++++++')
#         func()
#     return inner
#
# f = outer(func1)
# f()




# def outer(func):
#     def inner(age):
#         if age < 0:
#             age =0
#         func(age)
#     return inner
#
# @outer
# def say(age):
#     print("sunck is %d years old" %age)
#
#
# say(-10)


# def outer(func):
#     def inner(*args,**kwargs):
#         #添加修改的功能
#         print('&&&&&&&&&&&&')
#         func(*args,**kwargs)
#     return inner
#
# @outer
# def say(name,age):
#     print("my name is %s, I am %d years old" %(name,age))
#
#
# say('sunck',18)
i = 1
# import functools
#
#
# #偏函数 把一个参数固定住，形成一个新的函数
# int2 = functools.partial(int,base = 2)
#
# print(int('111'))
# print(int2('111'))

#异常处理 当程序遇到问题时不让程序结束，而是越过错误继续向下执行
'''
try......except......else
格式：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
......
except 错误码 as e:
    语句n
else:
    语句e
注意:else语句可有可无
作用:用来检测try语句块中的错误，从而让except语句捕获错误信息并处理
逻辑:当程序执行到try-except-else语句时
1.如果当try“语句t”执行出现错误，会匹配第一个错误码，如果匹配上就执行对应“语句”
2.如果当try“语句t”执行出现错误，没有匹配的异常，错误将会被提交到上一层的try语句，或者到程序的最上层
3.如果当try“语句t”执行没有出现错误，执行else下的“语句e”(前提是有else)
'''

# try:
#     print(3 / 1)
# # except NameError as e:
# #     print("没有该变量")
# except ZeroDivisionError as e:
#     print("除数为0了")
# else:
#     print("代码没有问题")
# finally:
#     print('结束了')
# #
# print("#############")

#使用except而不使用任何的错误类型
# try:
#     print(4 / 0)
# except:
#     print("程序出现了异常")
#
# #使用except带着多种异常
# try:
#     print(5 / 0)
# except (NameError,ZeroDivisionError):
#     print("出现了NameError或ZeroDivisionError")

#特殊
#1、错误其实是class(类),所有的错误都继承自BaseException,所以在捕获的时候，它捕获了该类型的错误,还把子类一网打尽
# try:
#     print(5 / 0)
# except BaseException as e:
#     print('异常1')
# except ZeroDivisionError as e:
#     print('异常2')

#2、跨越多层调用，main调用了func2，func2调用了func1，func1出现了错误，这时只要main捕获到了就可以处理
# def func1(num):
#     print(1 / num)
# def func2(num):
#     func1(num)
# def main():
#     func2(0)
#
# try:
#     main()
# except ZeroDivisionError as e:
#     print("出错了")


'''
try......except......else......finally
格式：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
......
except 错误码 as e:
    语句n
else:
    语句e
finally:
    语句f
注意:else、finally语句可有可无
作用:else用来检测try语句块中的错误，从而让except语句捕获错误信息并处理；finally语句t无论是否有错误都将执行最后的语句f
逻辑:当程序执行到try-except-else语句时
1.如果当try“语句t”执行出现错误，会匹配第一个错误码，如果匹配上就执行对应“语句”
2.如果当try“语句t”执行出现错误，没有匹配的异常，错误将会被提交到上一层的try语句，或者到程序的最上层
3.如果当try“语句t”执行没有出现错误，执行else下的“语句e”(前提是有else)
'''


'''
1、打开文件
open(path,flag[,encoding][,errors])
path:要打开文件的路径
flag：打开方式
r  以只读方式打开文件，文件的描述符放在文件的开头
rb 以二进制格式打开一个文件用于只读，文件的描述符放在文件的开头
r+ 打开一个文件用于读写，文件的描述符放在文件的开头
w  打开一个文件只用于写入，如果该文件已经存在会覆盖，如果不存在则创建新文件
wb 打开一个文件只用于写入二进制，如果该文件已经存在会覆盖，如果不存在则创建新文件
w+ 打开一个文件用于读写，如果该文件已经存在会覆盖，如果不存在则创建新文件
a  打开一个文件用于追加，如果文件存在，文件描述符将会放到文件末尾
a+ 打开一个文件用于读写，文件的描述符放在文件的末尾，读不到数据
encoding:编码方式
errors:错误处理
'''

# path = r'D:\pay\协议支付1期\data\1.txt'
#ignore 忽略错误
# f = open(path,'r',encoding='utf-8',errors='ignore')
# f = open(path,'r',encoding='utf-8')

'''
2、读文件内容
'''
#1、读取文件全部内容
# str1 = f.read()
# print(str1)

#2、读取指定字符数
# str2 = f.read(10)
# print('*'+str2+'*')
# str3 = f.read(10)
# print('*'+str3+'*')

#3、读取整行，包括“\n”字符
# str4 = f.readline()
# print(str4)
# str5 = f.readline()
# print(str5)

#4、读取整行的指定字符数
# str6 = f.readline(10)
# print(str6)

#5、读取所有行并返回列表
# str7 = f.readlines()
# print(str7)

#6、返回实际size字节的行（如每行10个字节，读15，返回两整行列表）
# str8 = f.readlines(1)
# print(str8)

#修改描述符的位置
# f.seek(10)
# str9 = f.read()
# print(str9)

'''
3、关闭文件
'''
# f.close()

#一个完整的过程
# 方法1
# try:
#     f1 = open(path,'r',encoding='utf-8')
#     print(f1.read())
# finally:
#     if f1:
#         f1.close()

# 方法二
# with open(path,'r',encoding='utf-8') as f2:
#     print(f2.read())


# path = r'D:\pay\协议支付1期\data\2.txt'
# f = open(path,'w')
#
# #写文件
# #1、将信息写入缓冲区
# f.write("sunck is a good man")
#
# #2、刷新缓冲区
# #直接把内部缓冲区的数据立刻写入文件，而不是被动的等待自动刷新缓冲区写入(关闭文件、缓冲区满)
# f.flush()
#
# f.close()
#
# with open(path,'a') as f2:
#     f2.write('good man')


import os

os.system('tasklist | findstr /C:"notepad.exe"')
