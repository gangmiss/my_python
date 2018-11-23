from greenlet import greenlet
import time

def func1():
    while True:
        print("--------A-------")
        g2.switch()
        time.sleep(1)

def func2():
    while True:
        print("--------B-------")
        g1.switch()
        time.sleep(1)


g1=greenlet(func1)
g2=greenlet(func2)

g1.switch()  #主动控制程序执行顺序