class Animal:
    def eat(self):
        print("吃")
    def run(self):
        print("跑")

    def __love(self):  #私有方法不能被继承
        print("恋爱")

class Cat(Animal):  #继承
    def catch(self):
        print("抓老鼠")

class Dog(Animal):
    def bark(self):
        print("叫")

    #重构
    def run(self):
        print("飞")

    def run(self):
        #如果我重构也要调用父类的run方法，则有两种写法：
        #Animal.run(self)
        super().run()
        print("飞")



tom=Dog()
tom.run()
tom.bark()
