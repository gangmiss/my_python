from threading import Thread, Lock
import time

b = 0


def func1():
    global b

    for i in range(1000000):
        lock.acquire()  # 如果是该线程先抢到锁，则另外的线程就会堵塞，知道该线程解开锁，其他的线程才解锁开始执行
        b += 1
        print("----func1----%d" % b)
        lock.release()


def func2():
    global b
    for i in range(1000000):
        lock.acquire()
        b += 1
        print("----func2----%d" % b)
        lock.release()


lock = Lock()

t1 = Thread(target=func1)
t1.start()

t2 = Thread(target=func2)
t2.start()

# 这句话一开始就打印了，没什么用
print("结果是：%d" % b)

# 线程抢着给b赋值，可能会造成同一时间取了相同的值就行赋值