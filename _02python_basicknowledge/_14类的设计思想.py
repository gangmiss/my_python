class Store(object):
    def product_a_car(self):
        pass
    def order(self,name):
        return self.product_a_car(name)  #工厂模式：自己不实现具体制造方法，由传递进来的对象自己实现

class BaoMaStore(Store):
    def product_a_car(self,name):
        return BaoMaCar(name).produce()

class BenchiStore(Store):
    def product_a_car(self,name):
        return BaoMaCar(name).produce()


class Car(object):
    def __init__(self,name):
        self.name=name
    def new_a_car(self):
        print("正在生产%s车"%self.name)
    def produce(self):
        return self.new_a_car()
    def go_run(self):
        print("%s生成完毕，我要去溜溜啦"%self.name)

class BaoMaCar(Car):
    def __init__(self,name):
        self.name=name
    def new_a_car(self):
        super().new_a_car()
        return BaoMaCar(self.name)


class BenchiCar(Car):
    def __init__(self,name):
        self.name=name
    def new_a_car(self):
        super().new_a_car()
        return BenchiCar(self.name)

car=BaoMaStore().order("x6宝马3系列")
car.go_run()
benchi=BenchiStore().order("奔驰5")
benchi.go_run()