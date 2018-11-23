"""
单播：一对一
多播：一对多
广播：一对所有
"""
#网络通讯只有两种：UDP，TCP
from socket import *
"""
udp:用户数据包协议，传输不稳定
"""
socket=socket(AF_INET,SOCK_DGRAM)
socket.setsockopt(SOL_SOCKET,SO_BROADCAST,1)#设置为广播模式
socket.sendto("hahaha",("<broadcast>",7788))


""""
tcp:传输控制协议，是一种面向连接的、可靠的、基于字节流的传输层通信协议，传输稳定，比udp速度要慢一点，web服务器都是用tcp
"""
"""服务器TCP"""
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",8899))
serverSocket.listen(5)  #linux系统无效，因为它自己会算一个出来，windows系统的意思是同一时间最多可以连接的socket个数
# serverSocket.setblocking(False)#设置为非堵塞
clientSocket,clientInfo=serverSocket.accept()#不停的等待客户端，然后创建新的通讯套接字，clientSocket是客户端的套接字，clientInfo是客户端的ip及port
recvData=clientSocket.recv(1024)#接收数据流
# sendData=clientSocket.send("123".encode("gb2312"))#发送数据流
clientSocket.close()

#如果服务器不通讯了，则关闭服务器套接字
serverSocket.close()


"""客户端TCP"""
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect(("192.169.6.128",8899))
clientSocket.send("124".encode("gb2312"))#发送数据流，不用sendto是因为已经跟别人连接了，直接说话就行了
# recvData=clientSocket.recv(1023)#接收数据流

clientSocket.close()






