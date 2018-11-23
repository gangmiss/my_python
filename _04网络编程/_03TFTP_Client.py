from threading import Thread
import struct
from socket import *


def main():

    class MyThread(Thread):
        def run(self):
            receive_data()


    def receive_data():
        f = open("D:/test.png", "ab+")
        while True:
            recvdata=udpsocket.recvfrom(1024)
            recv_msg=recvdata[0]
            msg=recv_msg[4:]
            f.write(msg)
            if msg=="":
                break
        f.close()

            # if a==1:
            #     #请求下载数据
            #     thread2=Thread(target=writeFile,args=(recv_ipdata,))
            #     thread2.start()
            # elif a==2:
            #     #请求上传数据
            #     pass
            # elif a==3:
            #     #传递数据
            #     pass
            # elif a==4:
            #     #确认回复
            #     pass
            # else:
            #     #error
            #     pass

    udpsocket=socket(AF_INET,SOCK_DGRAM)
    msg=struct.pack("!H8sb5sb",1,"test.png".encode("gb2312"),0,"octet".encode("gb2312"),0)
    udpsocket.sendto(msg,("192.168.6.128",7788))
    MyThread().start()

if __name__=="__main__":
    main()
