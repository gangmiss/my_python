a=100
b=a
print(id(a))
print(id(b))#b持有a的内存地址的引用

a2=[11,22]
b2=a2
a2.append(33)
print(a2)
print(b2)


a3="hello"
#a[0]="H" #报错，因为数字，字符串，元组在内存上不可修改，其他的类型都可以修改

a4=[11,22]
a4[0]=33
print(a4) #列表和字典可以修改