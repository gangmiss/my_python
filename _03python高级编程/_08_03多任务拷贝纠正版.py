from multiprocessing import Manager,Queue,Pool
import os

path="E:\英雄时刻\\2287817946"
new_path="D:\英雄时刻\\2287817946"
#复制文件
def copyFile(queue,fileName):
    fr=open(path+"\\"+fileName,"rb+")
    if os.path.exists(new_path):
        pass
    else:
        os.makedirs(new_path)
    path2=new_path+"\\"+fileName
    fw=open(path2,"wb+")
    content=fr.read()
    if content!="":
        fw.write(content)

    if queue.full()==False:
        queue.put(fileName)

    fr.close()
    fw.close()
def main():
    pool=Pool(5)
    listFiles=os.listdir(path=path)
    queue=Manager().Queue()
    for fileName in listFiles:
        pool.apply_async(copyFile,(queue,fileName,))

    names=[]

    num=0
    while num<len(listFiles):
        file_name=queue.get()
        names.append(file_name)
        num+=1
        print("%s复制完成，已完成%.2f%%"%(file_name,(num/len(listFiles))*100))
    pool.close()
    pool.join()
    print("复制完毕")
if __name__ == '__main__':
    main()