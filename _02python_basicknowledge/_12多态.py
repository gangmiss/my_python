class Dog:
    def print_self(self):
        print("大家好,我是一只狗，请多多关照")

class Xiao_Tian_Quan(Dog):
    def print_self(self):
        print("大家好，我是一个高级的狗，请大家听命于我")

class Tu_Gou(Dog):
    def print_self(self):
        print("大家好，我是一个土狗，请大家不要惹我")


def introduce_self(temp):  #定义的时候不知道调用哪个方法，你传进来谁，我就调用谁的方法
    temp.print_self()

introduce_self(Dog())
introduce_self(Xiao_Tian_Quan())
introduce_self(Tu_Gou())