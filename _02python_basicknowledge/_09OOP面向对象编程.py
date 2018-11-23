class Home: #类也需要存储空间，所以也可以理解为一个对象，称为类对象，即一切皆为对象
    """
    _xxx      不能用'from module import *'导入
    __xxx__ 系统定义名字
    __xxx    类中的私有变量名
    """
    #属性
    love=0  #这个称为类属性，所有对象共享这一个熟悉

    #限定这个类只能有这些对象属性(不包括类属性)
    __slots__ = ("area","money","info","containers","left_area")

    #方法
    def __init__(self,area,info):  #类里面的def叫方法，类外边的def叫函数，方法必须传递自己，函数可以没有参数
        self.area=area  #self对象添加一个area，这个称为对象属性，只跟单个的对象有关
        self.money=10000000
        self.info=info
        self.containers=[]
        self.left_area=self.area

    def __str__(self):
        msg="房子的总面积是%d,剩余面积是%d,户型是%s"%(self.area,self.left_area,self.info)
        msg+=",房子里面的床有："
        str=""
        for item in self.containers:
            str+=",%s"%item  #此item是对象，直接用对象的话，他的输出是item里面的__str__方法的返回值
        if str !="":
            str=str[1:]
        msg+=str
        return msg

    def __del__(self):   #如果有多个该类的引用对象，则在删除最后一个引用时我才被调用
        print("内存清楚的时候，我被调用")


    def __get_hourse_money(self):  #两个下划线属于私有方法，否则属于共有方法，可给对象调用
        return self.money

    def add_items(self,item):
        self.containers.append(item)
        self.left_area-=item.get_area()

class Bed:
    def __init__(self,name,area):
        self.name=name
        self.area=area

    def __str__(self):
        return self.name  #原来这里才是对象的输出
        # return self.name+"的面积的是%d"%self.area

    def get_name(self):
        return self.name
    def get_area(self):
        return self.area

fangzi=Home(129,"三室一厅一厨三卫")
bed=Bed("席梦思",6)
fangzi.add_items(bed)
bed=Bed("超软床",4)
fangzi.add_items(bed)

print(fangzi)

import sys
sys.getrefcount(fangzi) #查询Home的对象引用个数（比实际对象的个数会多一个，因为对象传递进去会多一个引用），如果fangzi的引用被删除，则程序会崩溃

