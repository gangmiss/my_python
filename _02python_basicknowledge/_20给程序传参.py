import sys

print(sys.argv) #运行程序时可以给程序传递参数，sys.argv来接收，是一个列表类型
name=""
if len(sys.argv)>1:
    name=sys.argv[1]

print(name)