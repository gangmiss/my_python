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





"""
搜集了一些python最重要的内建异常类名，并做了简单的介绍：
　　AttributeError：属性错误，特性引用和赋值失败时会引发属性错误
　　NameError：试图访问的变量名不存在
　　SyntaxError：语法错误，代码形式错误
　　Exception：所有异常的基类，因为所有python异常类都是基类Exception的其中一员，异常都是从基类Exception继承的，并且都在exceptions模块中定义。
　　IOError：一般常见于打开不存在文件时会引发IOError错误，也可以解理为输出输入错误
　　KeyError：使用了映射中不存在的关键字（键）时引发的关键字错误
　　IndexError：索引错误，使用的索引不存在，常索引超出序列范围，什么是索引
　　TypeError：类型错误，内建操作或是函数应于在了错误类型的对象时会引发类型错误
　　ZeroDivisonError：除数为0，在用除法操作时，第二个参数为0时引发了该错误
　　ValueError：值错误，传给对象的参数类型不正确，像是给int()函数传入了字符串数据类型的参数。
"""


