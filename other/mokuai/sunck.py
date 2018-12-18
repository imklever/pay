#coding:utf-8

#一个.py文件就是一个模块

# def sayGood():
#     print("sunck is a good man!")
#
# def sayNice():
#     print("sunck is a nice man!")
#
# def sayHandsome():
#     print("sunck is a handsome man!")
#
# TT = 100

# print("++++++")

#每一个模块都有一个__name__属性，当其值等于__main__时，表明该模块自身在执行。否则被引入其他文件
#当前文件如果为程序的入口文件，则__name__属性的值为__main__
if __name__ == "__main__":
    print("++++++")
else:
    print(__name__)
    def sayGood():
        print("sunck is a good man!")


    def sayNice():
        print("sunck is a nice man!")


    def sayHandsome():
        print("sunck is a handsome man!")


    TT = 100