infos={"name":"老王","address":"上海","age":27}#描述一个事物的不同类型建议使用字典，除了不可修改类型可以当作键值(只有数字，字符串，元组)，其他的能修改的类型都不能当作键
print("姓名%s，地址%s，年龄%d"%(infos["name"],infos["address"],infos["age"]))

print(len(infos))#取键值对个数
'''info_list_keys=infos.keys()
info_list_values=infos.values()''' #只有在Python2中才得到列表，Python3中会得到对象

for tem in infos.items():
    # print("元组：名字是%s，年龄是%s"%(tem[0],tem[1]))
    print(tem)

"""
#增
infos["QQ"]="10086"#如果没有QQ键，则新增，如果有这个键，则修改

#删
del infos["QQ"]#删除QQ键

#改
infos["name"]="隔壁老王"

#查
infos.get("QQ")


#1.打印提示系统
print("="*30)
print(" 1.添加一个名片")
print(" 2.删除一个名片")
print(" 3.修改一个名片")
print(" 4.查询一个名片")
print(" 5.查询所有名片")
print(" 6.退出系统")

users=[]

while True:
    # 2.提示用户输入
    index = int(input("请输入数字..."))

    # 3.执行功能
    if index==1:
        name = input("请输入名字...")
        addr = input("请输入地址...")
        age = input("请输入年龄...")
        user1={"name":name,"addr":addr,"age":age}
        users.append(user1)
        print(users)
    elif index==2:
        name1=input("请输入名字...")
        b=False
        for temp in users:
            if temp["name"]==name1:
                users.remove(temp)
                b=True;
                print("删除成功")
                break
        if not b:
            print("查无此人")
    elif index==3:
        name1 = input("请输入名字...")
        b = False
        for temp in users:
            if temp["name"] == name1:
                temp["name"]=input("请输入新的名字...")
                b = True;
                print("修改成功")
                print(users)
                break
        if not b:
            print("查无此人")
    elif index==4:
        name1 = input("请输入名字...")
        # b = False
        # for temp in users:
        #     if temp["name"] == name1:
        #         b = True;
        #         print("修改成功")
        #         print("姓名是%s，地址在%s，年龄是%s岁"%(temp["name"],temp["addr"],temp["age"]))
        #         break
        # if not b:
        #     print("查无此人")

        for temp in users:
            if temp["name"] == name1:
                b = True;
                print("修改成功")
                print("姓名是%s，地址在%s，年龄是%s岁" % (temp["name"], temp["addr"], temp["age"]))
                break
        else :
            print("查无此人")

    elif index==5:
        print("姓名\t地址\t年龄\t")
        for temp in users:
            print("%s\t%s\t%s岁\t"%(temp["name"],temp["addr"],temp["age"]))
    elif index==6:
        break
    else :
        print("输入有误，请重新输入...")"""
