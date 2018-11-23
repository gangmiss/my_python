a=[x for x in range(10)]
print(a)

b=(x for x in range(10))
print(b)

x=next(b)
print(x)



#斐波拉契数列（Fibonacci）

def createNum(number):
    print("-------开始-----------")         #因为是生成器，这句话不会打印
    a,b=0,1
    for x in range(number):
        yield b      #只要加上yield，这个函数就是生成器：仅仅保存了一套生成数据的算法，并没有真正执行，而是运行到yield就返回后面的值且程序暂停，调用next后才继续启动执行后面的
        a,b=b,a+b
    print("-------结束-----------")

generator_object=createNum(6)  #调用生成器不会执行函数，而是先返回一个生成器对象
print(next(generator_object))
print(next(generator_object))
print(generator_object.__next__())

for a in createNum(10):
    print(a)



#send方法
def create2():
    i=0
    while i<5:
        temp=yield i
        print(temp)
        i+=1
generator2=create2()
generator2.__next__()
generator2.send("哈哈哈")  #比next()高端一点，可以把哈哈哈复制给temp，但是如果是第一次就调用send，则必须send(None)才行