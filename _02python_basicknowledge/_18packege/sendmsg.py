def run1():
    print("111111111111111")

name="gangmiss"

#前置单下划线：包私有化，使用from somemodule import *导入的使用不了，因为Python把_name名字重整了，变成了_类名__name，
# 所以使用不了_name属性了，既然如此，那么可以使用更改后的名字也是可以调用的，同时使用import somemodule方式导入的和其他的都可以使用
_name="gangmiss2"