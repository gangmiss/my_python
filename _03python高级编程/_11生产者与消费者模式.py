from queue import Queue
from threading import Thread
import time

class Producer(Thread):
    def run(self):
        number=0
        global queue   #不修改他的值就可以不用global
        while True:
            if queue.qsize()<1000:
                for i in range(10):
                    number += 1
                    msg = "生成产品-%d" % (number)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Customer(Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize()>100:
                for i in range(3):
                    msg = "消费了包子-%s" % queue.get()
                    print(msg)
            time.sleep(1)



queue=Queue()
for i in range(500):
    queue.put("先生产一批包子-%d"%i)
for i in range(2):
    Producer().start()
for i in range(5):
    Customer().start()