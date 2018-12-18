#coding:utf-8

'''设计类
类名:见名知意，首字母大写，其他遵循驼峰原则
属性:见名知意，其他遵循驼峰原则
行为(方法/功能):见名知意，其他遵循驼峰原则
 '''

'''
类名:Wife
属性:sex age height weight faceVaule
行为:做饭 洗衣服 拖地 揉背 捶腿

类名:Husband
属性:sex age height weight faceVaule
行为:吃饭 看电视 打游戏 被揉背 被捶腿

类名:Car
属性:color type
行为:跑
'''

'''
创建类
类：一种数据类型，本身并不占内存空间，跟所学过的number，string，boolean等类似。用类创建实例化对象(变量)，对象占内存空间
格式：
class 类名(父类列表):
    属性
    行为
'''
#object:基类，超类，所有类的父类，一般没有合适的父类就写object
class Person(object):
    #定义属性
    name = "stu"
    age = 10
    height = 160
    weight = 80

    #定义方法
    #注意：方法的参数必须以self当第一个参数
    #self代表类的实例(某个对象)
    def run(self):
        print("run")
    def eat(self,food):
        print("eat "+food)
    def openDoor(self):
        print("我已经打开了冰箱门")
    def fillEle(self):
        print("我已经把大象装进冰箱了")
    def closeDoor(self):
        print("我已经关闭了冰箱门")

    def __init__(self):
        print("这里是init")
        pass


'''
实例化对象
格式：对象名 = 类名(参数列表)
注意：没有参数，小括号也不能省略
'''

#实例化一个对象
per1 = Person()
print(per1)
print(type(per1))
print(id(per1))

per2 = Person()
print(per2)
print(type(per2))
print(id(per2))


per = Person()
'''
访问属性
格式：对象名.属性名
赋值：对象名.属性名 = 新值
'''
per.name = 'Tom'
per.age = 18
# per.height = 170
per.weight = 70
print(per.name,per.age,per.height,per.weight)

'''
访问方法
格式：对象名.方法名(参数列表)
'''
per.openDoor()
per.fillEle()
per.closeDoor()

per.eat('apple')

#问题:目前来看Person创建的所有对象属性都是一样的
'''
对象的初始状态(构造函数)
构造函数：__init__() 在使用类创建对象的时候自动调用
注意：如果不显示的写出构造函数，默认会自动添加一个空的构造函数
'''
