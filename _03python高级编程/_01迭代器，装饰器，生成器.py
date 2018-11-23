"""
能够通过for依次取值的类型都是迭代器
list,tuple,dic,set,str
也可以通过isInstance()判断是否是Iterable对象
"""

from collections import Iterable
print(isinstance("abc",Iterable))

#生成器一定是迭代器
print((isinstance((x for x in range(10)),Iterable)))

#iter 转成迭代器
a=[1,2,3,4,5,6]
b=iter(a)
print(next(b))
