"""
tcp/ip协议(族)：用来规范网络数据传输通讯标准，使之遵循大家通用的一个数据传输协议
"""
#-*-coding=utf-8-*-
from socket import *
from multiprocessing import Process,Pool
from threading import Thread
import time,ctypes

udpsocket = socket(AF_INET, SOCK_DGRAM)
udpsocket.bind(("",7789))
class Client(Thread):
    def run(self):
        send_2_server()

class Service(Thread):
    def run(self):
        send_2_client()

def send_2_client():
    while True:
        recv_data = udpsocket.recvfrom(1024)
        service_msg, service_ipdata = recv_data
        msg = service_msg.decode("gb2312")
        if msg.lower() == "quit":
            print("服务器下线！")
            break
        print("服务器%s：%s" % (service_ipdata,msg))

def send_2_server():

    # str=b"1:1238605487:beauty:guiguzi:32:i love you"
    while True:
        msg=input("")
        # msg=b"tt"
        # msg.decode("utf-8")
        udpsocket.sendto(msg.encode("gb2312"), ('192.168.6.128', 7788))
        if msg=="quit":
            time.sleep(0.1)
            udpsocket.close()
            break

def main():
    # pool=Pool(5)
    # pool.apply_async(func=send_2_server)
    # pool.close()
    # pool.join()

    Client().start()
    Service().start()



def __del__():
    print("我下线了")

if __name__ == '__main__':
    main()

