from socket import *
from multiprocessing import Process

def main():
    def receive_data():
        while True:
            recvdata = udpsocket.recvfrom(1024)
            # user_msg=user_msg[2:-1]
            user_msg, ipdata = recvdata
            user_ip, user_port = ipdata
            user_msg = user_msg.decode("gb2312")
            if user_msg.lower() == "quit":
                print("%s用户下线" % user_ip)
                break
            print("%s(%d)用户：%s" % (user_ip, user_port, user_msg))

    udpsocket = socket(AF_INET, SOCK_DGRAM)
    udpsocket.bind(('', 7788))
    p = Process(target=receive_data)
    p.start()
    p.join()

if __name__ == '__main__':
    main()
