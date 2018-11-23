class Money(object):
    def __init__(self):
        self._num=100

    def setNumber(self,new_number):
        self._num=new_number
    def getNumber(self):
        return self._num
    number=property(getNumber,setNumber)

t=Money()
print(t.getNumber())
t.setNumber(200)
print(t.getNumber())

t.number=300  #使用了property他会调用setNumber(300)
print(t.number)  #使用了property他会调用getNumber()



"""第二种表达方式"""
class Person:
    def __init__(self):
        self.__age=18

    @property         #这叫装饰器
    def my_age(self):
        return self.__age

    @my_age.setter
    def my_age(self,new_age):
        self.__age=new_age

p=Person()
p.my_age=27
print(p.my_age)