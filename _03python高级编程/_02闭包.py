"""
在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的变量称之为闭包
"""

def fun1(a,b):

    def fun2(x):    #闭包函数
        return a*x+b

    return fun2   #返回函数的引用

res=fun1(2,3)(100)   #线性函数
print(res)








def w1(func):
    print("333333333333")
    print("定义的时候就开始装饰")
    def inner_func():
        #权限验证
        print("66666")
        return func
    return inner_func

def w2(func):
    print("55555555555")
    print("定义的时候就开始装饰")
    def inner_func():
        #权限验证
        print("7777777")
        return func
    return inner_func

@w1                      #装饰器，相当于f1=w1(f1)，执行这句调用就会打印3333333333
def f1():
    print("111111111111")

@w1
@w2
def f2():
    print("2222222222")

# f1=w1(f1)
# f1()

# f1()

f2()  #装饰是倒着装的，但是调用是正着调的，相当于一层一层往里面拆包  结果是55555,3333,6666,77777,222222
