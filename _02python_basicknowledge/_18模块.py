#coding=utf-8
#第一种方式引入
# from _02python_basicknowledge._18_01sendmessage import test1,test2
# from _02python_basicknowledge._18_01sendmessage import * #这种方式虽说可以引入所有的方法，但是不安全，如果其他的模块也有test1方法会覆盖前面的导入

# import _02python_basicknowledge._18_01sendmessage
# _02python_basicknowledge._18_01sendmessage.run1()
# _02python_basicknowledge._18_01sendmessage.run2()

#第二种方式引入   建议使用第二种方式
# import _02python_basicknowledge._18_01sendmessage
# _02python_basicknowledge._18_01sendmessage.test1()

# import _02python_basicknowledge._18_01sendmessage as tt  #取个简短的变量
# tt.run1()
# tt.run2()

from _02python_basicknowledge._18_01sendmessage import run2,run1
run2()
run1()


from _02python_basicknowledge._18packege import sendmsg
sendmsg.run1()
sendmsg.name

