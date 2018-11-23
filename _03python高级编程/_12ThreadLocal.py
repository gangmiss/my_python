import threading
from threading import Thread

thread_local=threading.local()

def process_student():
    stu=thread_local.student
    print("hello,%s,in(%s)"%(stu,threading.current_thread().name))  #获取自己的线程里面的对象的值


def process_thread(name):
    thread_local.student=name
    process_student()


t1=Thread(target=process_thread,args=("laowang",),name="Thread-A")
t2=Thread(target=process_thread,args=("laozhao",),name="Thread-B")
t1.start()
t2.start()
t1.join()
t2.join()