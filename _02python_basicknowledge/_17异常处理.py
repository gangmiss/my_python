try :
    open("xxx.txt","r")
    print("111111111111111")
except (NameError,IOError,FileNotFoundError):
    print("捕获到异常后的处理...")
except Exception as result:#result为异常对象的引用
    print(result)
    print("如果上面没有查到相应的异常类型，则我会调用")
else :
    print("如果上面没有异常出现，则我会调用，如果上面有异常，我不会调用")
finally:
    print("一定会执行")
print("2222222222222222222")


def test1():
    print("111111111111")
    print(5/0)
def test2():
    print("2222222222")
    test1()

def test3():
    print("33333333333333")
    try:
        test2()
    except Exception as ret:
        print(ret)
test3() #异常一直会向上传递，直达遇到异常处理，否则会到python解析器报错



#自定义异常
class InputShortException(Exception):
    def __init__(self,name,length):
        # super().__init__()
        self.name=name
        self.length=length

try:
    a=input("请输入至少3位数")
    if len(a)<=3:
        raise InputShortException(a,len(a)) #主动抛出异常
except InputShortException as result:
    print("捕获到自定义异常%s%d"%(result.name,result.length))


