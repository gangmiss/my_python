
g_sum=0#全局变量被函数调用也是要放在之前先定义的，全局建议已g_开头

def sum_2_nums():
    a=10
    b=20;
    print("%d+%d=%d"%(a,b,a+b))

def sum_2_nums2(a,b):
    return a+b;

def sum_2_nums3(result):
    print("结果是%d" % (result))

def return_list():
    a=10
    b=11
    c=12
    # d=(a,b,c)
    # d={"num1":a,"num2":b,"num3":c}
    d=[a,b,c]
    return d


def sum_2_num4():
    # sum=2
    global sum#申明这个是全局变量，不是局部变量了
    sum=4
    return sum
print(sum)

def sum_6(a,b=22,c=33):#缺省参数，后面不传的话就用默认的，必须写在后面
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"+str(a+b+c))

sum_6(33)
sum_6(33,55)
sum_6(33,55,66)
sum_6(33,c=66)#c=66命名参数


num1=int(input("请输入第一个数"))
num2=int(input("请输入第二个数"))

sum_2_nums()
sum_2_nums3(sum_2_nums2(num1,num2))
return_list()



def sum_7(a,b,*args):#不定长形参
    c=a+b#实参
    for temp in args:
        c+=temp
    print("求和%d"%c)
    return c
sum_7(1,2,3,4,4,5,6,7)#得到元组
sum_7(1,2)

def sum_8(a,b,**kwargs):#不定长形参
    c=a+b#实参
    print(a)
    print(b)
    print(kwargs)
    return c
sum_8(1,2,name=3,age=4)#得到字典


def sum_9(a,b,*args,**kwargs):#不定长形参
    c = a + b  # 实参
    print(a)
    print(b)
    print(args)
    print(kwargs)
    return c
a1=(33,44,55)
a2={"name":"老王","age":13}
sum_9(1,2,*a1,**a2)


def multiply_nums(a):
    if a==1:
        return 1
    return a*multiply_nums(a-1)
print(multiply_nums(int(input("请输入阶乘的数："))))