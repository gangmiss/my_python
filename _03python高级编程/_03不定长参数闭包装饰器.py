#通用装饰器(无参)：可以给需要的函数套上一层外衣
def w1(func):
    def func_in(*args,**kwargs):
        return func(*args,**kwargs)
    return func_in
@w1
def fun1(a,b):
    print("%s-----%s"%(a,b))
# @w1
# def fun1(*args,**kwargs):
#     print("%s-----%s"%(str(args),str(kwargs)))
fun1(44,55)




#通用装饰器(有参)：可以给需要的函数套上一层外衣
def w2(pre_arg):
    def w1(func):
        def func_in(*args,**kwargs):
            print(pre_arg)
            return func(*args,**kwargs)
        return func_in
    return w1
@w2("hahaha")   #通过这个参数，可以让装饰器做不同的事情
def fun2(a,b):
    print("%s-----%s"%(a,b))

fun2(55,66)



"""
变量的作用域遵循LEGB原则
L:local局部变量
E：enclosing闭包中常见
G:global全局变量
B：builtins系统内嵌
"""
