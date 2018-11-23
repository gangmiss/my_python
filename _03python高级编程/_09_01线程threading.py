import time
from threading import Thread
def func_sleep():
    print("11111")
    time.sleep(5)

for i in range(5):
    t=Thread(target=func_sleep)
    t.start()


print("2222222222")
#主线程要等所有子线程都执行完才程序结束

"""
僵尸进程：子进程死了结束了，但是父进程没有对子进程进行回收，则称为子进程为僵尸进程
孤儿进程：父进程死了结束了，子进程还没有死，则称为子进程为孤儿进程
0号进程(pid=0):负责切换进程
1号进程：负责生成所有进程(所有进程的爹,也是所有进程的收容所)
"""

class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("333333333")
            time.sleep(1)

thread=MyThread()
thread.start()