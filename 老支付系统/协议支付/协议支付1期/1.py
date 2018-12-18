#coding:utf-8
#list-tuple-dict-set的文件操作

import os

'''
os:包含了普通的操作系统的功能

'''

#获取操作系统类型 nt->windows posix->Linux、Unix或者Mac os X
print(os.name)

#打印操作系统详情的信息(windows不支持)
# print(os.uname)

#获取操作系统中的环境变量
print(os.environ)

#获取指定环境变量
print(os.environ.get('APPDATA'))

#获取当前目录
print(os.curdir)

#获取当前工作目录，即当前python脚本所在的目录
print(os.getcwd())

#以列表的形式返回指定目录下的所有的文件
print(os.listdir())

#在当前目录下创建目录
# os.mkdir('sunck')

#删除目录
# os.rmdir('sunck')

#获取文件属性
# print(os.stat('sunck'))

#重命名
# os.rename('sunck','kaige')

#删除普通文件
# os.remove('111.py')

#运行shell命令
# os.system('notepad')
# os.system('write')
# os.system('mspaint')
# os.system('msconfig')
# os.system('shutdown -s -t 5000')
# os.system('shutdown -a')
# os.system('tasklist | findstr /C:"notepad.exe"')
# os.system('taskkill /f /im notepad.exe')

#有些方法存在os模块里，还有些存在于os.path
#查看当前的绝对路径
print(os.path.abspath('./kaige'))

#拼接路径
p1 = r'D:\juhe\xieyinew'
p2 = 'kaige'
#注意：参数2里开始不要有斜杆
print(os.path.join(p1,p2))

#拆分路径（拆分最后模块）
path2 = r'D:\juhe\xieyinew\1.py'
print(os.path.split(path2))

#拆分获取最后模块的扩展名
print(os.path.splitext(path2))

#拆分获取最后模块的文件目录
print(os.path.dirname(path2))

#拆分获取最后模块的文件名
print(os.path.basename(path2))

#判断是否是目录
print(os.path.isdir(path2))

#判断文件是否存在
print(os.path.isfile(path2))

#判断目录或者文件是否存在
print(os.path.exists(path2))

#获取文件大小（字节）
print(os.path.getsize(path2))