class Base:
    def test(self):
        print("test")

class A(Base):
    def test1(self):
        print("test1")

class B:
    def test2(self):
        print("test2")

class C(A,B):   #多继承
    def test3(self):  #先找自己有没有test3方法，有就调用自己，否则再看A类有没有test3方法，否则再看B类有没有test3方法，否则再看Base类有没有test3方法，否则再看object类有没有test3方法
        print("test3")

c=C()
c.test()
c.test1()
c.test2()
c.test3()

print(C.__mro__)  #打印类的调用顺序（C3算法）