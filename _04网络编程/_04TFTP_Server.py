from threading import Thread
import struct
from socket import *


def main():
    def giveFile(recv_ipdata):
        f=open("./test.png","rb+")
        while True:
            filedata=f.read()
            msg=struct.pack("!H"+"%ds"%len(filedata)+"b5sb",3,filedata,0,"octet",0)
            udpsocket.sendto(msg,recv_ipdata)
            if msg=="":
                break

        f.close()

    def receive_data():
        while True:
            recv_msg,recv_ipdata=udpsocket.recvfrom(1024)
            print(str(recv_msg))
            a,b=struct.unpack("!HH",recv_msg[:4])
            if a==1:
                #请求下载数据
                thread2=Thread(target=giveFile,args=(recv_ipdata,))
                thread2.start()
            elif a==2:
                #请求上传数据
                pass
            elif a==3:
                #传递数据
                pass
            elif a==4:
                #确认回复
                pass
            else:
                #error
                pass

    udpsocket=socket(AF_INET,SOCK_DGRAM)
    thread=Thread(target=receive_data)
    thread.start()
    thread.join()

if __name__=="__main__":
    main()
