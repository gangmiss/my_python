#===============================变量开始======================

"""score = 100 #定义一个变量
score2=input("请输入分数") #提示用户输入
print("score变量里的值是%d"%score)
print("score变量里的值是%s,score2的值是%s"%(score,score2))

name = "东哥"
print("名字是：%s"%name)"""

str="[11,22,33]"
print(eval(str)) #可以去掉双引号


# False 有："",0,{},[],None
# True 有："a",1,{"a":1},[1]    0表示假，非0表示真

# a='lao'
# b='wang'
# c="===%s==="%(a+b)
# print(c)

a="abcdef hello word"
print(a[3])
print(a[len(a)-1])
print(a[-1])
print(a[2:5])
print(a[2:-1])#取从第三位到倒数第2个
print(a[2:])#取从第三位到最后
print(a[2:-1:2])#取从第三位到倒数第2个且隔一个取数
print(a[-1:0:-1])#倒叙到时去掉了第一位
print(a[-1::-1])#倒叙
print(a[::-1])#倒叙

#find
print(a.find("cd"))#从左边找，返回索引数
print(a.rfind("cd"))#从右边找，返回索引数
print(a.index("cd"))#从左边找，有则返回索引数，无则报错
print(a.rindex("cd"))#从右边找，有则返回索引数，无则报错

#count
print(a.count("cd"))#有多少个cd

#replace
print(a.replace("cd","xy"))#从左往右全部替换
print(a.replace("cd","xy",1))#只替换一个

#splite
print(a.split("cd"))#返回列表类型[]
print(a.split())#切割所有乱七八糟的符号和空格

#capitalize
print(a.capitalize())#首字母大写

#title
print(a.title())#每个单词的首字母大写

#startswith
print(a.startswith("cd"))

#endswith
print(a.endswith("cd"))

#lower
print(a.lower())

#upper
print(a.upper())

#ljust
print(a.ljust(100))#在长度为100的字符串长度里a靠左显示

#rjust
print(a.rjust(100))

#center
print(a.center(100))#在长度为100的字符串长度里a居中显示

#lstrip
print(a.lstrip())#删除左侧空格

#rstrip
print(a.rstrip())

#strip
print(a.strip())#删除两侧空格

#partition
print(a.partition("cd"))#从左边开始分割成左边一波，右边一波，自己一波，返回元组类型()
print(a.rpartition("cd"))#从右边开始分割成左边一波，右边一波，自己一波，返回元组类型()

#splitlines
print(a.splitlines())#按行分割，返回列表

#isalpha
print(a.isalpha())#判断是否是字母

#isdigit
print(a.isdigit())#判断是否是数字

#isalnum
print(a.isalnum())#判断是否是纯字母和数字

#isspace
print(a.isspace())#判断是否是纯空格

#join
b=["aaa","bbb","ccc"]
c=" "
print(c.join(b))#将b列表通过c来连接


#==============================结束=======================

#============================数据类型开始===================

#1.numbers(int,float,long)
#2.布尔类型（true,false）
#3.string字符串类型
#4.List列表类型
#5.Tuple元组类型
#6.Dictionary字典类型

# age=input("请输入年龄")
# age=int(age)
# print(type(age))#输出类型

#============================数据类型结束===================

#=======================判断语句开始====================

# if age==18:
#     print("我是美少女")
# elif age>18:
#     print("就业了")
# else :
#     print("学习")

# age1=10
# age2=30
# if age1<=15 or age2>=25:
#     print("1111111111111111")
# elif age1==10 and age2==30:
#     print("好"*10)
#
# if not (age1<=15 or age2>=25):
#     print("33333333333333")
#
# while age2<40:
#     age2+=1
#     print("age2="+str(age2))

#=======================判断语句结束====================

#输出所有关键字
# import keyword
# print(keyword.kwlist)

#======================运算符开始=====================
# a=5
# b=2
# c="Hello"
# print(a+b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a-b)
# print(a%b)
# print(a**b)
# print(c*10)
#======================运算符结束=====================


#===================九九乘法表开始==================
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print("%d*%d=%d\t"%(j,i,j*i),end="")#print自带换行，加上end=""后就不会换行了        j+=1
#     i+=1
#     print("")
#===================九九乘法表结束==================

#====================for循环开始===================
a="laowang"
for temp in a:
    print(temp)

for temp in a:
    print(temp)
    break
else :
    print("只有执行了break，我才不会输出，否则一定会输出")


"""注意这里有坑的"""
a=[11,22,33,44,55,66]
for i in a:
    print(i)
    if i==33 or i==44:  #删除33和44，但是结果只是删了33，因为删除33后角标往后移了一位，而44往前补了一位，就漏掉了44的判断
        a.remove(i)
#====================for循环结束===================

