a=100#不可变类型，a的值不会因为函数的调用而改变
b=[100]#可变类型，b的值会因为函数的调用而改变
def func1(num):
    num+=num#先看num是可变还是不可变，如果是可变，则修改num的引用的值，如果是不可变，则新定义一个num值进行输出
    # num=num+num #重新定义了一个局部变量，全局变量依然不变，而上面那个没有重新定义，只是修改num引用里面的值，所以num+=num与num=num+num不同，只是计算值相等而已
    print(num)

func1(a)
print(a)

func1(b)
print(b)
