import os
import sys
import time

#创建进程方式有：fork，process，pool

res=os.fork()         #创建一个进程，即多了一个任务，然而windows不能用，Because forking is ingrained in the Unix programming model, though, this script works well on Unix, Linux, and modern Macs
if res==0:  #子进程
    while True:
        print("111111111")
        time.sleep(1)
else :
    while True:
        print("2222222222")
        time.sleep(1)




print("----------------------------------")
res=os.fork()
if res==0 :
    print("11111") #打印一次
else :
    print("22222222") #打印一次

res2=os.fork()  #后面新创建的两个子线程从这里开始执行
if res==0 :
    print("333333") #打印两次
else :
    print("444444") #打印两次



print("----------------------------------")
res=os.fork()
if res==0 :
    print("11111") #打印一次
else :
    print("22222222") #打印一次

    res2=os.fork()
    if res==0 :
        print("333333") #打印一次
    else :
        print("444444") #打印一次


"""
fork炸弹
while True:
    os.fork()
"""