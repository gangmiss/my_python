names=["laoliu",100,3.14,"laowang"]#描述大量相同型建议使用列表

#增
names.append("老杨")#增加一个元素
names.insert(0,"八戒")
names2=["葫芦娃","猴子"]
print(names+names2)#合并进去但不改变names
print(names.extend(names2))#合并列表，追加到后面且改变names值

#删
names.pop()#删除最后一个（栈：先进后出，后进先出的特点）
names.remove("老杨")#从左删一个
del names[1]#删除第二个元素
# del names[2:5] #删第三个到底六个
# del names[-1]# 删除最后一个
# del names[2:]# 删除从第三个到最后

#改
names[0]="猪八戒"

#查
print("猪八戒" in names)
print("猪八戒" not in names)


#排序
names.sort()#从小到大排序
names.sort(reverse=True)#从大到小排序
names.reverse()#倒叙

infors=[{"name":"laowang","age":"18"},{"name":"xiaoli","age":"20"}]
infors.sort(key=lambda x:x['name'])