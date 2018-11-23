'''

1.如果一个包很好用，在包的当前目录里新建一个set.py文件
2.编辑set.py，写入如下内容
from distutils.core import setup
setup(name="gangmiss",version="1.1",description="描述",author="gangmiss",py_modules=["suba.aa","suba.bb"])
3.运行命令：sudo python3 setup.py build
4.运行命令：sudo python3 setup.py sdist
5.把包安装到系统就可以随处调用了：sudo python3 setup.py install
'''