#coding=utf-8
def mult_f(a,b,func):
    return func(a,b)

result=mult_f(11,22,lambda x,y:x+y)#匿名函数当作实参传递
print(result)


# result=mult_f(11,33,input("请输入一个匿名函数："))#Python2：只有在运行时才知道怎么运行，这就是Python动态语言的特性
result=mult_f(11,33,eval(input("请输入一个匿名函数：")))#Python3：只有在运行时才知道怎么运行，这就是Python动态语言的特性，而C和java都是必须先确定怎么做才执行
print(result)



#交换两个变量的值
a=4
b=5

#第一种
c=a
a=b
b=c

#第二种
a=a+b
b=a-b
a=a-b

#第三种
a,b=b,a
