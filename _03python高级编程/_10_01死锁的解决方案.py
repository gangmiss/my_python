"""
死锁：两个线程都在等待对方释放锁，结果都没有释放，占用着线程锁
"""
from threading import Thread,Lock
import time

class ThreadA(Thread):
    def run(self):
        print("1111111111")
        time.sleep(1)
        if ta.acquire():
            print("------1--------")
            if tb.acquire(timeout=2):   #非堵塞(看门狗)：等它2秒钟，如果占用他的线程还没有释放锁，我就不堵塞在这了，直接false之后往下走
                print("----------111---------")
            ta.release()

class ThreadB(Thread):
    def run(self):
        print("2222222222")
        time.sleep(1)
        if tb.acquire():
            print("------2--------")
            if ta.acquire(timeout=2):
                print("----------222---------")
            tb.release()


ta=Lock(2)
tb=Lock(2)
ThreadA().start()
ThreadB().start()
