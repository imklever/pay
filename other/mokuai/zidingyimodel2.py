#coding:utf-8

#引入模块
#from ...... import语句
#作用：从模块中导入一个指定的部分到当前命名空间

#格式：from module import name1[,name2[,...namen]]
from sunck import sayGood,sayNice,TT


'''
程序内容的函数可以将模块中的同名函数覆盖
def sayGood():
    print("*********")
'''


sayGood()
sayNice()
print(TT)