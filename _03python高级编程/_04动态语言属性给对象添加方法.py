import types
class Person:
    num=100
    def __init__(self,newName):
        self.name=newName

def run(self):
    print("%s在跑"%self.name)

@staticmethod               #定义类时就初始化，可由类和对象调用
def eat():
    print("在吃" )

@classmethod                 #只能由类调用,不能用对象调用
def fly(self):
    print("%s飞翔"%self.num )

p1=Person("老王")
p1.run=types.MethodType(run,p1)   #动态给对象添加方法
p1.run()

Person.eat=eat
p1.eat()

Person.fly=fly
Person.fly()
