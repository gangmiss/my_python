from multiprocessing import Process
import time

def func1():
    while True:
        print("11111111")
        time.sleep(1)

p=Process(target=func1)
p.start()    #如果使用的是Process创建字进程，主进程必须等到所有的子进程都结束，主进程才结束
p.join() #堵塞：等到所有子进程都结束，我才往下走（join([timeout]):等待的最长的超时时间，见到形参带中括号的意思是可传可不传数值）
p.terminate()#强制结束自己进程

