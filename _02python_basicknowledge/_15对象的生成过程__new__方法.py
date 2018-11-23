class Dog(object):
    #初始化实例属性，在__new__方法调用后返回的对象引用做为参数传递进去
    def __init__(self):
        print("调用init方法")

    #打印对象实例时的输出
    def __str__(self):
        print("调用了str方法")

    #对象的地址空间回收时调用
    def __del__(self):
        print("调用了del方法")

    #返回生成对象的引用
    def __new__(cls, *args, **kwargs):#Dog类对象，元组形参，字典形参
        print("调用了new方法")
        return object.__new__(cls)

dog=Dog()