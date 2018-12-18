#coding:utf-8
'''
self代表类的实例，而非类
哪个对象调用方法，那么该方法中的self就代表那个对象
self.__class__ 代表类名_
'''

class Person(object):
    def run(self):
        print("run")
        print(self.__class__)
        p = self.__class__('tt',30,10,30)
        print(p)
    def eat(self,food):
        print("eat "+food)
    def say(self):
        print("Hello! my name is %s, I am %d years old!" %(self.name,self.age))
    #self不是关键字，换成其他的标识符也是可以的，但是常用self
    def play(a):
        print('play '+a.name)

    def __init__(self,name,age,height,weight):
        self.name = name
        self.age =age
        self.height = height
        self.weight = weight

per1 = Person('tom',20,160,80)
per1.say()
per1.play()
per1.run()

per2 = Person('hanmeimei',21,161,81)
per2.say()
