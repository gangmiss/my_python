"""import gevent
def func1(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(1)
g1=gevent.spawn(func1,5)
g2=gevent.spawn(func1,5)
g3=gevent.spawn(func1,5)
g1.join()
g2.join()
g3.join()"""

import gevent
from gevent import socket,monkey
monkey.patch_all()  #修改Python源代码进行协程操作

def func1(socket):
    while True:
        recvData=socket.recv(1024)
        if recvData:
            print("接收的内容：%s"%recvData)
            socket.send(recvData)
        else:
            socket.close()
            break

def main():
    sSocket=socket.socket()
    sSocket.bind(("",7788))
    sSocket.listen(1000)
    while True:
        cSocket,cAddr=socket.accept()#等待的时候自动切换其他的线程
        gevent.spawn(func1,cSocket)


if __name__ == '__main__':
    main()

