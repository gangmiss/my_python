#GIL(全局解释器锁):Python保证只有一个线程在被cpu使用，有两个线程，有三个cpu，此时并不是两个线程都被cpu使用，而是只有一个线程正在一个cpu使用，另外一个cpu属于空闲状态
#Python里面多进程比多线程效率高，但是多进程参数传递费力，如果我一定要是使用线程怎么办呢，为了解决GIL问题，我把其中的一个线程用c语言写

"""
gcc xxx.c -shared -o libxxx.so
gcc loop.c -shared -o libdeadloop.so

loop.c的内容是：
#include "studio.c"
int main(){
    while (1):
    {
        ;
    }
}

"""

from ctypes import *
from threading import Thread

lib=cdll.LoadLibrary("./libdeadloop.so")#加载c语言so文件
t=Thread(target=lib.DeadLoop)    #子线程死循环
t.start()

while True:  #主线程死循环
    pass

#因为Python并没有真正解决多线程问题，而底层C语言可以真正实现多线程，所以不调用Python的线程，调用C语言的线程这样就解决了GIL问题

