#coding:utf-8

class Person(object):
    def run(self):
        print("run")
    def eat(self,food):
        print("eat "+food)
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age =age
        self.height = height
        self.weight = weight

per = Person('hanmeimei',20,170,55)
per.age = 10
print(per.age)