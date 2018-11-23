class Dog(object):
    __instance=None
    __init_flag=False
    def __new__(cls,name, *args, **kwargs):
        if cls.__instance==None:
            cls.__instance=object.__new__(cls)
            return cls.__instance
        else :
            return cls.__instance

    def __init__(self,name):
        if Dog.__init_flag==False:  #只初始化一次
            Dog.__init_flag=True
            self.name=name

    def get_name(self):
        return self.name


a=Dog("旺财")
print(a.get_name())
b=Dog("Tom")
print(b.get_name())#虽说只生成一个对象，但是却初始化了两次
print(id(a))
print(id(b))