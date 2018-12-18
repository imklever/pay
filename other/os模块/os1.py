#OS模块

import os

#getcwd() 获取当前工作目录(当前工作目录默认都是当前文件所在的文件夹)
result = os.getcwd()
print(result)

#listdir() 获取指定文件夹中所有内容的名称列表
result = os.listdir(r'D:\juhe\other')
print(result)

#mkdir()  创建文件夹
# os.mkdir('girls')
# os.mkdir('boys')

#rmdir() 删除空目录
# os.rmdir('girls')
# os.rmdir('boys')


#makedirs()  递归创建文件夹
# os.mkdir(r'D:\pay\other\os模块\a\b\c\d\e')
# os.makedirs(r'D:\pay\other\os模块\a\b\c\d\e\f')

#rmdir() 删除空目录
os.rmdir(r'D:\juhe\other\os模块\a\b\c\d\e\f')
