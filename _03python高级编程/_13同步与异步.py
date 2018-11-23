"""
同步调用就是你喊你朋友吃饭，你朋友在忙，你就在那等，一直等他忙完了，然后你们一起去吃饭
异步调用就是你喊你朋友吃饭，你朋友说知道了，待会我忙完了去找你，你先忙别的
"""
from multiprocessing import Pool
import time,os

def main():
    def func1():
        print("进程池中的进程：%d----%d"%(os.getpid(),os.getppid()))
        for i in range(3):
            print("-------%d-------"%i)
            time.sleep(1)
        return "hahaha"

    def func2(arg):
        print("----pid=%d--"%os.getpid())
        print("------arg=%s"%arg)


    pool=Pool(3)
    pool.apply_async(func=func1,callback=func2)

    while True:
        time.sleep(1)
        print("-------主进程pid=%d"%os.getpid())


if __name__ == '__main__':
    main()