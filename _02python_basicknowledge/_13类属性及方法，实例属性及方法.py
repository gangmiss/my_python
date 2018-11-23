class Game:
    #类属性
    person_numbers=0

    #静态方法
    @staticmethod
    def print_title():
        Game.person_numbers=100
        print("跟类一起创建生成，但是需要手动调用才能运行")

    #类方法
    @classmethod    #装饰器
    def get_numbers(cls):
        cls.person_numbers+=1;
        print(cls.person_numbers)
        return cls.person_numbers

    #实例方法
    def add_person(self,name):

        self.name=name#实例属性

        print("添加一个人")
        Game.get_numbers()

game=Game()
game.print_title()
game.add_person("gangmiss")
Game.get_numbers()