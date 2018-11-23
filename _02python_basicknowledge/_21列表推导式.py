

print(range(10,18,2))#没隔2一次取一个数，返回一个列表的引用，真正用到的时候才会给你列表

for temp in range(10,18):
    print(temp)

a=[i for i in range(10,18)]  #列表推导式（列表生成式）
a=[i for i in range(10,18) if i%2==0]

print(a)

b=[(i,j) for i in range(3) for j in range(4)]
print(b)